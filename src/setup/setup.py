import subprocess
import sys
import time
import warnings
import os
from typing import List, Dict, Optional
from pathlib import Path
from rich.progress import Progress, BarColumn, TextColumn, TimeRemainingColumn

from src.config.colors import Colors as C
from src.config.ui_helper import UI
from src.config.banners import Banners as B

def install_package(package_name: str) -> bool:
    try:
        UI.processing(f"Installing {package_name}...")
        subprocess.run(
            [sys.executable, '-m', 'pip', 'install', package_name],
            capture_output=True, text=True, check=True
        )
        return True
    except Exception:
        return False

def check_package(package_name: str) -> bool:
    if package_name == 'spotdl':
        warnings.filterwarnings("ignore", category=UserWarning, module="spotdl")
    try:
        __import__(package_name.replace('-', '_'))
        return True
    except ImportError:
        return False

def check_external_tool(tool_name: str, version_flags: Optional[List[str]] = None) -> bool:
    if version_flags is None:
        version_flags = ['--version', '-v', '-version']
    for flag in version_flags:
        try:
            subprocess.run([tool_name, flag], capture_output=True, text=True, check=True, timeout=5)
            return True
        except (subprocess.CalledProcessError, FileNotFoundError, subprocess.TimeoutExpired):
            continue
    return False

def add_to_path(tool_name: str):
    if sys.platform == "win32":
        try:
            path = os.environ['PATH']
            if tool_name not in path:
                os.environ['PATH'] = f"{path};{os.path.dirname(sys.executable)}"
                UI.success(f"{tool_name.upper()} added to PATH")
        except Exception:
            UI.error(f"{tool_name.upper()} failed to add to PATH")

def setup_environment(required_packages: Optional[List[str]] = None,
                      external_tools: Optional[Dict[str, List[str]]] = None) -> bool:

    if required_packages is None:
        required_packages = ['yt-dlp', 'spotdl', 'rich']
    if external_tools is None:
        external_tools = {'ffmpeg': ['-version']}

    UI.print_banner("setup")
    print()
    print(B.box_message("STEP 1: COMPONENT CHECK"))
    print()

    all_items = required_packages + list(external_tools.keys())
    all_tools_ok = True
    missing_packages = []
    missing_tools = []

    with Progress(
        TextColumn("[bold white]{task.fields[name]}[/bold white]"),
        BarColumn(bar_width=None),
        TextColumn("[green]{task.percentage:>3.0f}%"),
        TimeRemainingColumn(),
        transient=True,
    ) as progress:

        task = progress.add_task("check", total=len(all_items), name="Initializing...")

        for item in all_items:
            progress.update(task, name=f"Checking {item.upper()}")
            time.sleep(0.5)  # имитация проверки

            if item in required_packages:
                if check_package(item):
                    UI.success(f"{item.upper()}")
                else:
                    UI.error(f"{item.upper()}")
                    all_tools_ok = False
                    missing_packages.append(item)
            else:
                if check_external_tool(item):
                    UI.success(f"{item.upper()}")
                else:
                    UI.error(f"{item.upper()}")
                    all_tools_ok = False
                    missing_tools.append(item)

            progress.update(task, advance=1)
    print()
    print(B.box_message("COMPONENT CHECK COMPLETE"))
    print()

    # Установка недостающих компонентов
    if not all_tools_ok:
        response = UI.prompt("Would you like to install missing components? (y/n): ")
        if response.lower() in ['yes', 'y']:
            print()
            print(B.box_message("STEP 2: INSTALLING MISSING COMPONENTS"))

            with Progress(
                TextColumn("[bold white]{task.fields[name]}[/bold white]"),
                BarColumn(bar_width=None),
                TextColumn("[green]{task.percentage:>3.0f}%"),
                TimeRemainingColumn(),
                transient=True,
            ) as install_progress:

                install_task = install_progress.add_task("install", total=len(missing_packages)+len(missing_tools), name="Installing...")

                # Установка pip-пакетов
                for pkg in missing_packages:
                    install_progress.update(install_task, name=f"Installing {pkg.upper()}")
                    success = install_package(pkg)
                    if success:
                        UI.success(f"{pkg.upper()} installed successfully")
                    else:
                        UI.error(f"{pkg.upper()} installation failed")
                    install_progress.update(install_task, advance=1)

                # Проверка внешних инструментов
                for tool in missing_tools:
                    install_progress.update(install_task, name=f"Checking {tool.upper()}")
                    if check_external_tool(tool):
                        UI.success(f"{tool.upper()} is now available")
                        add_to_path(tool)
                    else:
                        UI.error(f"{tool.upper()} still not found")
                    install_progress.update(install_task, advance=1)

            # Финальная проверка
            all_tools_ok = all(check_package(p) for p in required_packages) and all(check_external_tool(t) for t in external_tools.keys())

    # Создание файла .setup_done
    if all_tools_ok:
        setup_dir = Path('./src/setup')
        setup_dir.mkdir(parents=True, exist_ok=True)
        setup_file = setup_dir / '.setup_done'
        with open(setup_file, 'w') as f:
            f.write('Setup completed successfully.')
        UI.info("Setup completed. The installer will not run again.")

    return all_tools_ok

if __name__ == "__main__":
    setup_environment()

import os

def get_installed_php_versions():
    """Get installed PHP versions."""
    php_versions = []
    with os.popen('update-alternatives --display php') as f:
        lines = f.readlines()
        for line in lines:
            if line.strip().startswith('/usr/bin/php'):
                parts = line.strip().split(' ')
                if len(parts) > 0:
                    php_versions.append(parts[0])
    return php_versions

def install_php_version(version):
    """Install PHP version."""
    os.system(f"sudo apt install php{version} php{version}-cli")

def uninstall_php_version(version):
    """Uninstall PHP version."""
    os.system(f"sudo apt remove php{version} php{version}-cli")

def change_php_version():
    """Change PHP version in the system."""
    php_versions = get_installed_php_versions()
    if not php_versions:
        print("No installed PHP versions found.")
        return

    print("Available PHP versions:")
    for index, version in enumerate(php_versions):
        print(f"{index + 1}. {version.replace('/usr/bin/php', '')}")

    print("a. Add a new PHP version")
    print("d. Remove a PHP version")

    choice = input("Choose a PHP version number to use (or 'q' to exit): ")

    if choice.lower() == 'q':
        return

    if choice.lower() == 'a':
        new_version = input("Enter the version number of the new PHP version to install: ")
        if new_version in php_versions:
            print(f"Version {new_version.replace('/usr/bin/php', '')} is already installed.")
        else:
            install_php_version(new_version)
            print(f"PHP version {new_version} has been successfully installed.")
    elif choice.lower() == 'd':
        version_to_remove = input("Enter the PHP version number to remove: ")
        try:
            version_to_remove = int(version_to_remove)
            if version_to_remove > 0 and version_to_remove <= len(php_versions):
                uninstall_php_version(php_versions[version_to_remove - 1].replace('/usr/bin/php', ''))
                print(f"PHP version {php_versions[version_to_remove - 1].replace('/usr/bin/php', '')} has been successfully removed.")
            else:
                print("Invalid version number.")
        except ValueError:
            print("Invalid version number.")
    else:
        try:
            choice = int(choice)
            if choice > 0 and choice <= len(php_versions):
                chosen_version = php_versions[choice - 1]
                os.system(f"sudo update-alternatives --set php {chosen_version}")
                print(f"PHP version has been changed to {chosen_version.replace('/usr/bin/php', '')}.")
            else:
                print("Invalid version number.")
        except ValueError:
            print("Invalid input.")

if __name__ == "__main__":
    change_php_version()

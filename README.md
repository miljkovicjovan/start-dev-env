# Script to start development environment

With this script you can quickly launch all your applications and websites needed for your development.
Available for Windows with plans to develop for Linux and macOS.

## Set up

1. Clone the repository.
2. Create a .env file in the root folder.
3. In the .env file add the following line "WINDOWS_USERNAME=user". (Replace user with your Windows username.)
4. Create a bat file:
```bash
@echo off
python "{path to project folder}\start-dev-env\start_dev_env.py" %*
```
5. Add the bat file's path to your PATH to make it accesible globally.
6. Modify the python script with the applications and websites you want.
7 Run the command:
```bash
start-dev-env
```

## Future Plans
- [ ] Create a application folder for modifying apps and websites to open.
- [ ] Create profiles, for example "programming", "video editing" or "gaming" for different apps and websites.
- [ ] Open up for Linux and macOS.

## Contibutions
Cotributions are welcome make sure to open an issue or PR with detailed explanation of your changes/improvements.

# Claude Code

{% embed url="https://docs.anthropic.com/en/docs/agents-and-tools/claude-code/overview" %}

1. To get to WSL...
   1. Open Powershell as an administrator
   2. Type WSL
   3. Off you go...

This error occurs due to PowerShell's execution policy restricting unsigned scripts. Here's how to resolve it:

1. Open PowerShell as Administrator
2. Run this command to check current execution policy:

```powershell
Get-ExecutionPolicy
```

3. If it's set to "Restricted", change it with:

```powershell
Set-ExecutionPolicy RemoteSigned
```

This allows locally created scripts and signed scripts from the internet to run. When prompted, confirm by typing "Y".

After changing the execution policy, you should be able to run npm commands. If you're concerned about system security, you can:

* Set the policy to "AllSigned" for stricter control
* Temporarily bypass for a single script using the `-ExecutionPolicy Bypass` flag
* Verify the script's origin before running

Would you like me to elaborate on any of these steps?

For installing Claude Code in a Windows Subsystem for Linux (WSL) terminal, here are the key steps:

1. Make sure you have:
   * WSL installed
   * Node.js and npm installed within your WSL distribution
   * Sufficient permissions to install global packages
2. Open your WSL terminal and run:

```bash
npm install -g @anthropic-ai/claude-code --force --no-os-check
```

A few potential troubleshooting tips:

* If you encounter permission issues, try using `sudo`:

```bash
sudo npm install -g @anthropic-ai/claude-code --force --no-os-check
```

* Ensure your Node.js version is compatible (check with `node --version`)
* You might need to configure npm global path permissions

You don't need to create a VM. WSL provides a Linux environment directly on Windows. However, if you're experiencing persistent installation issues, alternatives include:

* Using Docker
* Using a full Linux VM
* Installing directly on a native Linux system

Would you like me to help you diagnose any specific installation errors you're encountering?

I'll provide a step-by-step guide to ensure you have WSL, Node.js, and npm set up correctly:

1. Check WSL Installation:

```powershell
wsl --status
```

If not installed, open PowerShell as Administrator and run:

```powershell
wsl --install
```

2. Install Node.js in WSL: Open your WSL terminal and run:

```bash
# Update package lists
sudo apt update

# Install Node.js and npm
curl -fsSL https://deb.nodesource.com/setup_lts.x | sudo -E bash -
sudo apt-get install -y nodejs

# Verify installation
node --version
npm --version
```

3. Configure npm Global Permissions:

```bash
# Create a directory for global packages
mkdir -p ~/.npm-global

# Configure npm to use this directory
npm config set prefix '~/.npm-global'

# Add to PATH in .bashrc
echo 'export PATH=~/.npm-global/bin:$PATH' >> ~/.bashrc
source ~/.bashrc
```

4. Check Permissions:

```bash
# Verify you can install global packages
npm install -g npm@latest
```

Pro tips:

* Use `nvm` (Node Version Manager) for more flexible Node.js management
* The `sudo` prefix ensures you have sufficient permissions
* Always run `sudo apt update` before installing new packages

Would you like me to elaborate on any of these steps?

If you're getting "sudo not found", it typically means you're using a minimal WSL distribution that doesn't include sudo by default. Here's how to fix this:

For Ubuntu or Debian-based WSL distributions:

```bash
# Update package lists
apt update

# Install sudo
apt install sudo

# Now you can use sudo
sudo apt update

# Which package manager are you using?
which apk || which apt || which yum || which dnf
```

For Alpine Linux WSL:

```bash
# Install sudo
apk add sudo
```

For Fedora/RHEL-based distributions:

```bash
# Install sudo
dnf install sudo
```

Quick check:

1. Confirm your WSL distribution:

```bash
cat /etc/os-release
```

This will help determine the exact commands needed to install sudo. Most Ubuntu-based WSL installations come with sudo, so this is unusual. Could you share the output of `cat /etc/os-release` so I can provide more precise guidance?

apk = Alpine

```bash
# Update package index
apk update

# Install Node.js and npm
apk add nodejs npm

# Verify installations
node --version
npm --version

# Now install Claude Code
npm install -g @anthropic-ai/claude-code --force --no-os-check
```

If you encounter any permission issues, you might need to:

```bash
# Add global npm path to your PATH
echo 'export PATH=~/.npm-global/bin:$PATH' >> ~/.bashrc
source ~/.bashrc
```

Potential troubleshooting:

*   If Node.js/npm installation fails, try:

    ```bash
    apk add nodejs-current npm
    ```


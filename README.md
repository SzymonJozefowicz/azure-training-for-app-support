# Azure for Application Support

#### Part 1: Azure Fundametals

Topics:

Azure Tenants  
Identity AAD  
Subscriptions  
Regions  
Types of resources IaaS,PaaS,SaaS,KaaS  
Types of access RBAC  
Resource Groups  
Creating resource group using

    * portal
    * cli
    * powershell
    * terraform
    * biceps
Storage Accounts  
Virtual Networks  
Virtual Machines  
Recovery Service  
Monitoring and Alerts  

#### Links:
[Azure Documentation](https://docs.microsoft.com/en-us/azure/?product=popular)  
[Microsoft Learn](https://docs.microsoft.com/en-us/learn/)  
[Azure Concepts](https://docs.microsoft.com/en-us/learn/modules/fundamental-azure-concepts/)  


#### Sample code:
```git clone https://github.com/Azure-Samples/html-docs-hello-world.git```


### Required tools
#### Windows Subsystem for Linux
[How to install WSL2](https://docs.microsoft.com/en-us/windows/wsl/install)

#### Git  
[How to install Git on Ubuntu 20.04](https://linuxconfig.org/how-to-install-git-on-ubuntu-20-04-lts-focal-fossa-linux)

    sudo apt update
    sudo apt install git

#### Azure CLI
[How to install Azure Command Line Interface](https://docs.microsoft.com/en-us/cli/azure/install-azure-cli-linux?pivots=apt)

    curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash


#### Powershell
[How to install Powershell on Linux](https://docs.microsoft.com/en-us/powershell/scripting/install/install-ubuntu?view=powershell-7.2)


    # Update the list of packages
    sudo apt-get update
    # Install pre-requisite packages.
    sudo apt-get install -y wget apt-transport-https software-properties-common
    # Download the Microsoft repository GPG keys
    wget -q https://packages.microsoft.com/config/ubuntu/20.04/packages-microsoft-prod.deb
    # Register the Microsoft repository GPG keys
    sudo dpkg -i packages-microsoft-prod.deb
    # Update the list of packages after we added packages.microsoft.com
    sudo apt-get update
    # Install PowerShell
    sudo apt-get install -y powershell
    # Start PowerShell
    pwsh


#### Terraform

[How to install Terraform](https://learn.hashicorp.com/tutorials/terraform/install-cli)


    sudo apt-get update && sudo apt-get install -y gnupg software-properties-common curl
    curl -fsSL https://apt.releases.hashicorp.com/gpg | sudo apt-key add -
    sudo apt-add-repository "deb [arch=amd64] https://apt.releases.hashicorp.com $(lsb_release -cs) main"
    sudo apt-get update && sudo apt-get install terraform








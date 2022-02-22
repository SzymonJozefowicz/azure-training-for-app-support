# Azure for Application Support

## Part 1: Azure Fundametals

Topics:
#### Meeting 1
* Azure Tenants  
* Identity AAD  
* Subscriptions  
* Regions  
* Types of resources IaaS,PaaS,SaaS,KaaS  
* Types of access RBAC  
* Resource Groups  
#### Meeting 2
* Creating resource group using

    - portal
    - cli
    - terraform

* Storage Accounts  

#### Meeting 3
* Virtual Machines
* Virtual Networks  
 
#### Meeting 4 

* Bastion Hosts  
* Recovery Service   
* Monitoring and Alerts for VM

## Part 2: Running Applications in Azure

Topics:

#### Meeting 5 

* [Containers Basics](https://azure.microsoft.com/en-us/overview/what-is-a-container/#overview)    
* [Compute Services in Azure - VM vs ACI vs AKS vs Web App vs Static Web Pages](https://docs.microsoft.com/en-us/azure/architecture/guide/technology-choices/compute-decision-tree)  
* [Load balancing - Frond Door, Load Balancers,Application Gateway as Traffic Managers](https://docs.microsoft.com/en-us/azure/architecture/guide/technology-choices/load-balancing-overview)  
* [Applicaton Security](https://docs.microsoft.com/en-us/azure/architecture/framework/security/design-app-dependencies)  
* [Monitoring and Alerts for Applications](https://docs.microsoft.com/en-us/azure/azure-monitor/app/app-insights-overview)

#### Part 3: Deploying Applications in Azure

Topics:
* Code versioning using Git
* Building application  
* Building containerized application  
* Deploying application to VM  
* Deploying application to Web App Service  
* Deploying application to K8s (AKS)  
* API Deployments using APIM
* DevOps, DevSecOps, GitOps  
  
#### Part 4: Operation and maintenance of Applications in Azure

Topics:
* Configuration as a code
* Application Insights
* Monitoring application on VM
* Monitoring aplication on Web App Service
* Monitring application on K8s (AKS)
* Monitoring APIs using APIM


#### Links:
[Azure Documentation](https://docs.microsoft.com/en-us/azure/?product=popular)  
[Microsoft Learn](https://docs.microsoft.com/en-us/learn/)  
[Azure Concepts](https://docs.microsoft.com/en-us/learn/modules/fundamental-azure-concepts/)  
[Powershell ARM](https://docs.microsoft.com/en-us/azure/azure-resource-manager/management/manage-resources-powershell)


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





#### Sample scripts

az group create --name eur-infra-sandbox-szymon-rg --location westeurope --tags Owner='Szymon Jozefowicz' Project='Azure For App Support' Environment='Sandbox' Application='Azure For App Support'


### Sample App Insights Application
  
  
[NodeJS Sample App](https://github.com/Azure-Samples/Application-Insights-Click-Plugin-Demo)

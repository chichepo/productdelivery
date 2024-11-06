import json
from datetime import datetime, time
from abc import ABC, abstractmethod
from typing import List



# Define Product class
class Product:
    def __init__(self, name: str, scheduled_time: str, deployers: List['Deployer'], notifiers: List['Notifier']):
        self.name = name
        self.scheduled_time = scheduled_time
        self.deployers = deployers
        self.notifiers = notifiers



    def build(self):
        print(f"{datetime.now()} - Building {self.name}")



    def deploy(self):
        for deployer in self.deployers:
            deployer.deploy(self.name)



    def notify(self):
        for notifier in self.notifiers:
            notifier.notify(self.name)



    def run_pipeline(self):
        print(f"Running pipeline for {self.name} at scheduled time: {self.scheduled_time}")
        self.build()
        self.deploy()
        self.notify()



# Deployers Interface
class Deployer(ABC):
    @abstractmethod
    def deploy(self, product_name: str):
        pass



class ArtifactoryDeployer(Deployer):
    def deploy(self, product_name: str):
        print(f"{datetime.now()} - Deploying {product_name} to Artifactory")



class NexusDeployer(Deployer):
    def deploy(self, product_name: str):
        print(f"{datetime.now()} - Deploying {product_name} to Nexus")



class S3Deployer(Deployer):
    def deploy(self, product_name: str):
        print(f"{datetime.now()} - Deploying {product_name} to S3")



# Notifiers Interface
class Notifier(ABC):
    @abstractmethod
    def notify(self, product_name: str):
        pass



class EmailNotifier(Notifier):
    def notify(self, product_name: str):
        print(f"{datetime.now()} - Notifying via Email about {product_name}")



class SlackNotifier(Notifier):
    def notify(self, product_name: str):
        print(f"{datetime.now()} - Notifying via Slack about {product_name}")



# Main function to load config and run pipeline
def load_config_and_run_pipeline(config_path: str):
    with open(config_path, 'r') as f:
        config = json.load(f)



    for product_config in config["products"]:
        deployers = []
        for target in product_config["deploy_targets"]:
            if target == "Artifactory":
                deployers.append(ArtifactoryDeployer())
            elif target == "Nexus":
                deployers.append(NexusDeployer())
            elif target == "S3":
                deployers.append(S3Deployer())



        notifiers = []
        for channel in product_config["notification_channels"]:
            if channel == "Email":
                notifiers.append(EmailNotifier())
            elif channel == "Slack":
                notifiers.append(SlackNotifier())



        product = Product(
            name=product_config["name"],
            scheduled_time=product_config["scheduled_time"],
            deployers=deployers,
            notifiers=notifiers
        )



        # For simplicity, just run the pipeline now
        product.run_pipeline()



# Assuming config.json contains our pipeline configuration
if __name__ == "__main__":
    load_config_and_run_pipeline("config.json")
 
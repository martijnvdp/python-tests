from ansible.inventory.manager import InventoryManager
from ansible.parsing.dataloader import DataLoader
from pathlib import Path
import pytest
import unittest.mock


@pytest.fixture
def ansibleInventory():
    loader = DataLoader()
    loader.set_basedir("./")
    inventory = InventoryManager(
        loader=loader,
        sources=f"{Path(__file__).resolve().parent}/inventory",
    )
    with unittest.mock.patch(
        "my_ansible_function.InventoryManager", return_value=inventory
    ):
        yield inventory

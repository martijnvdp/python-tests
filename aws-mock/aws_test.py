import logging
from pathlib import Path
import sys

rootDir = f"{Path(__file__).resolve().parent}/"
logger = logging.getLogger(__name__)

# add parent path for import parrent functions
sys.path.insert(0, f"{Path(__file__).resolve().parent.parent.parent}")


def testCreateValidAWSSecet(secretsmanager):
    secret = '"test":"test123"'
    result = secretsmanager.create_secret(
        Name="test-secret",
        SecretString=secret,
    )
    logger.info(result)
    assert result["ARN"]
    assert result["Name"] == "test-secret"
    secret_value = secretsmanager.get_secret_value(SecretId="test-secret")
    logger.info(secret_value)
    assert secret_value["SecretString"] == secret

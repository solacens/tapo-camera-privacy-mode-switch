from pytapo import Tapo
from dynaconf import Dynaconf

settings = Dynaconf()

cameras = [Tapo(ca.host, ca.user, ca.password) for ca in settings.camera_accounts]


def set_privacy_mode(enabled: bool) -> None:
    for camera in cameras:
        camera.setPrivacyMode(enabled)


if __name__ == "__main__":
    set_privacy_mode(True)

from pydantic_settings import BaseSettings, SettingsConfigDict


class ConfigApp(BaseSettings):
    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8')

    project_name: str
    authjwt_secret_key: str


class ConfigDB(BaseSettings):
    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8', env_prefix='db')

    user: str
    password: str
    name: str
    host: str
    port: int

    @property
    def get_uri(self) -> str:
        return 'postgresql://{}:{}@{}:{}/{}'.format(self.user, self.password, self.host, self.port, self.db)


config_app = ConfigApp()
config_db = ConfigDB()

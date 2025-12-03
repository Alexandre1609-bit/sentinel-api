from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    #On définit les variables qu'on veut RENDRE configurables
    app_name: str = "Sentinel-API Default"
    app_version: str = "1.0.0"
    admin_email: str #Si pas de valeur par défaut = OBLIGATOIRE !!

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore" #'Extra=ignore' Dit à Pyantic que les "champs supplémentaires" (extra) trouvés
        #dans le '.env' ne sont pas des erreurs.
    )

#On instancie la config une fois pour pouvoir l'importer ailleurs
settings = Settings()
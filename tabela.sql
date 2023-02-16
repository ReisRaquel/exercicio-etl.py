
CREATE TABLE relatorio_unido (
    id INT IDENTITY(1,1) PRIMARY KEY,
    pais VARCHAR(50) NOT NULL,
    estado VARCHAR(50) NOT NULL,
    populacao VARCHAR (50) not NULL,
    media_de_renda VARCHAR(50) NOT NULL
);
CREATE DATABASE ratesapp;
GO

USE ratesapp;
GO

DROP TABLE IF EXISTS Rates;
GO

CREATE TABLE Rates (
    RatesID INT NOT NULL IDENTITY(1,1) PRIMARY KEY CLUSTERED,
    ClosingDate DATE,
    CurrencySymbol NVARCHAR(3),
    ExchangeRate DECIMAL(18,10)
);
GO

INSERT INTO Rates (ClosingDate, CurrencySymbol, ExchangeRate) VALUES ('2019-01-03', 'EUR', 0.8812125485);
GO

SELECT * FROM Rates;
GO
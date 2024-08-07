DROP TABLE IF EXISTS jkacosta91_coderhouse.idealista;

CREATE TABLE IF NOT EXISTS jkacosta91_coderhouse.idealista (
    propertyCode VARCHAR(250) ENCODE ZSTD,  -- Unique identifier for the property
    thumbnail VARCHAR(250) ENCODE ZSTD,  -- URL of the thumbnail image
    numPhotos INT ENCODE ZSTD,  -- Number of photos available
    floor VARCHAR(50) ENCODE ZSTD,  -- Floor level of the property (optional)
    price DECIMAL(10, 2) ENCODE ZSTD,  -- Price of the property (optional)
    propertyType VARCHAR(50) ENCODE ZSTD,  -- Type of property (studio, flat, etc.)
    operation VARCHAR(50) ENCODE ZSTD,  -- Kind of operation (rent or sale)
    size INT ENCODE ZSTD,  -- Size of the property (in square meters)
    exterior BOOLEAN ENCODE ZSTD,  -- Indicates if the property has an exterior space
    rooms INT ENCODE ZSTD,  -- Number of rooms
    bathrooms INT ENCODE ZSTD,  -- Number of bathrooms
    address VARCHAR(250) ENCODE ZSTD,  -- Address of the property
    province VARCHAR(250) ENCODE ZSTD,  -- Province where the property is located
    municipality VARCHAR(250) ENCODE ZSTD,  -- Municipality where the property is located
    district VARCHAR(250) ENCODE ZSTD,  -- District within the municipality
    neighborhood VARCHAR(250) ENCODE ZSTD,  -- Neighborhood within the district
    country VARCHAR(50) ENCODE ZSTD,  -- Country where the property is located
    latitude DECIMAL(10, 6) ENCODE ZSTD,  -- Geographic latitude
    longitude DECIMAL(10, 6) ENCODE ZSTD,  -- Geographic longitude
    showAddress BOOLEAN ENCODE ZSTD,  -- Indicates if the address is publicly shown
    url VARCHAR(250) ENCODE ZSTD,  -- URL of the property listing on Idealista
    agency BOOLEAN ENCODE ZSTD,  -- Indicates if the property is listed by an agency
    favourite BOOLEAN ENCODE ZSTD,  -- Flag indicating if the property is marked as favorite
    hasVideo BOOLEAN ENCODE ZSTD,  -- Indicates if the property has a video tour
    status VARCHAR(50) ENCODE ZSTD,  -- Status of the property (good, refurbished, etc.)
    age VARCHAR(50) ENCODE ZSTD,  -- Age of the property (e.g., builtInThe70s)
    newDevelopment BOOLEAN ENCODE ZSTD,  -- Indicates if the property is part of a new development
    newProperty BOOLEAN ENCODE ZSTD,  -- Indicates if the property is newly listed
);
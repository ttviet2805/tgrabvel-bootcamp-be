
# Tgrabvel Backend Project

This project provides a RESTful API to manage city data. It includes endpoints to retrieve city information and nearby cities based on location clusters.

## Getting Started

To use this project, follow the steps below:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/ttviet2805/tgrabvel-bootcamp-be.git
   ```

2. **Navigate to the `api` directory**:
   ```bash
   cd api
   ```

3. **Install dependencies**:
   ```bash
   npm install
   ```

4. **Start the server**:
   ```bash
   npx nodemon server
   ```

## API Endpoints

### Retrieve a List of Cities

- **Endpoint**: `/api/cities`
- **Method**: `GET`
- **Description**: Returns a list of city names from the `city` collection.

### Retrieve Nearby Cities

- **Endpoint**: `/api/nearby-city/{cityName}`
- **Method**: `GET`
- **Description**: Returns a list of cities that have the same `loc_clusters` value as the input city, excluding the input city itself.
- **Parameters**:
  - `cityName` (string): Name of the city to find nearby cities for.

### Attraction Details

- **Endpoint**: `/api/attraction-detail/{name}`
- **Method**: `GET`
- **Description**: Retrieves details for a specified attraction, including related hotels and restaurants within the same state.

### Add a Review

- **Endpoint**: `/api/add-review`
- **Method**: `POST`
- **Description**: Allows users to post a review for a specific attraction.

### Top Trending Attractions

- **Endpoint**: `/api/top-trending-attractions`
- **Method**: `GET`
- **Description**: Returns the top 30 trending attractions based on a weighted score from user ratings.

### Recommendations by State

- **Endpoint**: `/api/recommendations/{state}`
- **Method**: `GET`
- **Description**: Provides a list of recommended attractions for a specified state, utilizing a Python script for data processing.

## Swagger Documentation

The API includes Swagger documentation, which can be accessed at `/docs` after starting the server.

## Database Connection

The API connects to a MongoDB Atlas database with the database name `tgrabvel`.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

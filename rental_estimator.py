class RentalEstimator:
    def __init__(self, base_price_per_bedroom, location_factor):
        self.base_price_per_bedroom = base_price_per_bedroom
        self.location_factor = location_factor

    def estimate_rent(self, num_bedrooms, location):
        # Calculate base rent
        base_rent = num_bedrooms * self.base_price_per_bedroom

        # Apply location factor
        location_rent = base_rent * self.location_factor[location]

        # Calculate total rent
        total_rent = base_rent + location_rent
        return total_rent


# Example usage:
if __name__ == "__main__":
    # Define base prices and location factors
    base_price_per_bedroom = 1000
    location_factors = {"downtown": 1.5, "suburb": 1.2, "rural": 1.0}

    # Create an instance of the RentalEstimator
    estimator = RentalEstimator(base_price_per_bedroom, location_factors)

    # User inputs
    num_bedrooms = int(input("Enter the number of bedrooms: "))
    location = input("Enter the location (downtown, suburb, rural): ")

    # Estimate rent
    estimated_rent = estimator.estimate_rent(num_bedrooms, location)

    # Display the result
    print(f"Estimated rent for a {num_bedrooms}-bedroom apartment in {location}: ${estimated_rent}")

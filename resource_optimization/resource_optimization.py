from scipy.optimize import minimize

def irrigation_schedule(soil_moisture, weather_forecast):
    def objective(x):
        return (x[0] - soil_moisture)**2
    
    result = minimize(objective, [0.5], bounds=[(0.0, 1.0)])
    return result.x

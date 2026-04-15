"""
Triangle Angle Calculator
Calculates the third angle of a triangle when two angles are known.
The sum of all angles in a triangle is always 180 degrees.
"""

def calculate_third_angle(angle1, angle2):
    """
    Calculate the third angle of a triangle.
    
    Args:
        angle1 (float): First angle in degrees
        angle2 (float): Second angle in degrees
    
    Returns:
        float: Third angle in degrees
    
    Raises:
        ValueError: If angles are invalid
    """
    if angle1 <= 0 or angle2 <= 0:
        raise ValueError("Angles must be positive values")
    
    if angle1 >= 180 or angle2 >= 180:
        raise ValueError("Each angle must be less than 180 degrees")
    
    third_angle = 180 - angle1 - angle2
    
    if third_angle <= 0:
        raise ValueError("Sum of angles cannot equal or exceed 180 degrees. The two provided angles are too large.")
    
    return third_angle

def validate_triangle(angle1, angle2, angle3):
    """
    Validate if three angles form a valid triangle.
    
    Args:
        angle1 (float): First angle in degrees
        angle2 (float): Second angle in degrees
        angle3 (float): Third angle in degrees
    
    Returns:
        bool: True if angles form a valid triangle
    """
    if angle1 <= 0 or angle2 <= 0 or angle3 <= 0:
        return False
    
    if abs(sum([angle1, angle2, angle3]) - 180) < 0.0001:  # Account for floating point errors
        return True
    
    return False

def main():
    """Main function to run the triangle angle calculator."""
    print("=" * 50)
    print("TRIANGLE ANGLE CALCULATOR")
    print("=" * 50)
    print("Enter two angles of a triangle to calculate the third angle.")
    print("(All angles in degrees)")
    print()    
    try:
        angle1 = float(input("Enter first angle: "))
        angle2 = float(input("Enter second angle: "))
        
        third_angle = calculate_third_angle(angle1, angle2)
        
        print()
        print("=" * 50)
        print("RESULTS:")
        print(f"Angle 1: {angle1}°")
        print(f"Angle 2: {angle2}°")
        print(f"Angle 3: {third_angle}°")
        print()\n        print(f"Sum of angles: {angle1 + angle2 + third_angle}°")
        
        # Validate the triangle
        is_valid = validate_triangle(angle1, angle2, third_angle)
        print(f"Valid triangle: {is_valid}")
        print("=" * 50)
        
    except ValueError as e:
        print(f"\nError: {e}")
    except ValueError as e:
        print(f"\nError: Invalid input. Please enter numeric values.")


if __name__ == "__main__":
    main()
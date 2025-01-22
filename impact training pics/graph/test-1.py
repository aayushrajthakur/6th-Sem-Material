def max_interviews(n, interviews, v):
    """
    Calculates the maximum number of interviews that can be attended.

    Args:
        n: The number of interviews.
        interviews: A list of tuples, where each tuple represents an interview
            with the format (x, t), where x is the coordinate of the interview
            and t is the time of the interview.
        v: The maximum speed.

    Returns:
        A tuple containing two integers:
            - The maximum number of interviews that can be attended if starting
              from x = 0.
            - The maximum number of interviews that can be attended if starting
              from any point.
    """

    # Sort interviews by time
    interviews.sort(key=lambda x: x[1])

    # Calculate the maximum number of interviews starting from x = 0
    max_interviews_from_zero = 0
    current_time = 0
    current_position = 0

    for x, t in interviews:
        # Calculate the distance to the interview
        distance = abs(x - current_position)
        # Calculate the time required to reach the interview
        time_required = distance / v
        # Check if we can reach the interview on time
        if current_time + time_required <= t:
            max_interviews_from_zero += 1
            current_time = t
            current_position = x

    # Calculate the maximum number of interviews starting from any point
    max_interviews_from_any_point = 0

    for i in range(n):
        current_time = 0
        current_position = interviews[i][0]
        count = 0

        for j in range(i, n):
            x, t = interviews[j]
            distance = abs(x - current_position)
            time_required = distance / v
            if current_time + time_required <= t:
                count += 1
                current_time = t
                current_position = x

        max_interviews_from_any_point = max(max_interviews_from_any_point, count)

    return max_interviews_from_zero, max_interviews_from_any_point

# Read input
n = int(input("Enter the number of interviews: "))
interviews = [tuple(map(int, input("Enter the coordinate and time of interview (x t): ").split())) for _ in range(n)]
v = int(input("Enter the maximum speed: "))

# Get the results
max_from_zero, max_from_any_point = max_interviews(n, interviews, v)

# Print the results
print(max_from_zero)
print(max_from_any_point)
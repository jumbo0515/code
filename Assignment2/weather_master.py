"""
File: weather_master.py
Name:jumbo
-----------------------
This program should implement a console program
that asks weather data from user to compute the
average, highest, lowest, cold days among the inputs.
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""
# This constant controls when to stop
EXIT = -1


# sentinel value


def main():
    """
    That asks weather data from user to compute the average, highest, lowest, cold days among the inputs.
    """
    print('StandCode " Weather Master 4.0 "!')
    data = int(input('Next Temperature : ( or' + str(EXIT) + ' to quit)? '))
    if data == EXIT:
        print('No temperatures were entered')
    else:
        maximum = data
        minimum = data
        cold = 0
        step = 1
        total = data
        average = 0
        while True:
            data = int(input('Next Temperature : (or' + str(EXIT) + ' to quit)? '))
            if data == EXIT:
                break
            if maximum < data:
                maximum = data
            if minimum > data:
                minimum = data
            if data < 16:
                cold += 1
            step += 1
            total += data
            average = total / step
        print('Highest temperature = ' + str(maximum))
        print('Lowest temperature = ' + str(minimum))
        print('Average = ' + str(average))
        print(str(cold) + ' cold day(s)')

    # data = int(input('Data: '))
    # if data == EXIT:
    #     print('No temperatures were entered')
    # else:
    #     maximum = data
    #     while True:
    #         data = int(input('Data: '))
    #         if data == EXIT:
    #             break
    #         if maximum < data:
    #             maximum = data
    #     print('Highest temperature = ' + str(maximum))
    # if minimum = data
    # 	 while True:
    # 		data = int(input('Data: '))
    # 		if data == EXIT:
    # 			break
    # 		if minimum > data:
    # 			minimum = data
    #         print('Lowest temperature = ' + str(maximum))


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
    main()

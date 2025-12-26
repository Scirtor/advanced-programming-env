import a3task1 as task1
import a3task2 as task2
import a3task3 as task3
import a3task4 as task4
import a3task5 as task5
import a3task6 as task6
import a3task7 as task7
import a3task8 as task8


def main():

    choice = int(input("""Enter your choice: 
                       1. Area of the shape        | Sum and mean of the arrays
                       2. Hexagons are bestagons   | Area of the Rectangles
                       3. Right Triangles(really?) | Alphabetically correct
                       4. Fraction dividor         | How many points in the circle
                       5. Fraction subtractor      | All the possible divisors ever
                       6. GCD and LCM              | Area of a quadrilateral
                       7. XYZT, what this even mean| Integer into octal code
                       8. Natural dividable        | 1D array replacement
                       """))
    match choice:
        case 1:
            subchoice = int(input("""Which one exactly:
                                  1. Area of the shape
                                  2. Sum and mean of the arrays
                                    \n"""))
            match subchoice:
                case 1:
                    task1.area_of_shape()
                case 2:
                    task1.sum_and_mean()
        case 2:
            subchoice = int(input("""Which one exactly:
                                  1. Hexagons are bestagons
                                  2. Area of the rectangles
                                    \n"""))
            match subchoice:
                case 1:
                    task2.bestagons()
                case 2:
                    task2.area_of_triangle()
        case 3:
            subchoice = int(input("""Which one exactly:
                                    1. Right Triangles(really?)
                                    2. Alphabetically correct
                                    \n"""))
            match subchoice:
                case 1:
                    task3.right_triangles()
                case 2:
                    task3.alphabetically_correct()
        case 4:
            subchoice = int(input("""Which one exactly:
                                1. Fraction dividor
                                2. How many points in the circle
                                \n"""))
            match subchoice:
                case 1:
                    task4.fraction_dividor()
                case 2:
                    task4.points_in_circle()
        case 5:
            subchoice = int(input("""Which one exactly:
                                    1. Fraction subtractor
                                    2. All the possible divisors ever
                                    \n"""))
            match subchoice:
                case 1:
                    task5.fraction_subtractor()
                case 2:
                    task5.all_divisors()
        case 6:
            subchoice = int(input("""Which one exactly:
                                    1. GCD and LCM
                                    2. Area of a quadrilateral
                                    \n"""))
            match subchoice:
                case 1:
                    task6.gcd_and_lcm()
                case 2:
                    task6.area_of_quadrilateral()
        case 7:
            subchoice = int(input("""Which one exactly:
                                    1. XYZT, what this even mean
                                    2. Integer into octal code
                                    \n"""))
            match subchoice:
                case 1:
                    task7.xyzt()
                case 2:
                    task7.integer_to_octal()
        case 8:
            subchoice = int(input("""Which one exactly:
                                    1. Natural dividable
                                    2. 1D array replacement
                                    \n"""))
            match subchoice:
                case 1:
                    task8.natural_dividable()
                case 2:
                    task8.array_replacement()
    return


if __name__ == "__main__":
    main()
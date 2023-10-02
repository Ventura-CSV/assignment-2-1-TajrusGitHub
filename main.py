def main():
    num_males = int(input('Enter the number of male students: 15'))
    num_females = int(input('Enter the number of female students: 19'))

    total_students = num_males + num_females
    m_perc = (num_males / total_students) * 100
    f_perc = (num_females / total_students) * 100

    print(f'The total number of students:\t{total_students}')
    print(f'The number of males and females:\t{num_males}\t{num_females}')
    print(f'The percentage of males and females:\t{m_perc:.2f}%\t\t{f_perc:.2f}%')

    return m_perc, f_perc

if __name__ == '__main__':
    main()

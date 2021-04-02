# encoding:utf-8
import pickle
import req


def main():

    while (True):
        req.show_choices()
        choice = input('Enter choice(1-4):  ')
        print()

        if choice == '1':
            req.write_record()

        elif choice == '2':
            req.read_records()

        elif choice == '3':

            rafTur = input('Rafın türünü giriniz : ')
            rafKat = int(input('Rafın katını giriniz : '))
            rafNo = int(input('Rafın Nosunu giriniz : '))
            rafIndex = int(input('Rafın indexini giriniz : '))
            req.search_record(rafTur, rafKat, rafNo, rafIndex)

        elif choice == '4':
            break

        else:
            print('Invalid input')





# call the main function.
main()
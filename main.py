# encoding:utf-8
import pickle
import req
import string


def main():

    while (True):
        req.show_choices()
        choice = input('Enter choice(1-4): ')
        print()

        if choice == '1':
            req.write_record()

        elif choice == '2':
            req.read_records()

        elif choice == '3':

            rafTur = input('Rafın türünü giriniz : ')
            rafKat = input('Rafın katını giriniz : ')
            rafNo = input('Rafın Nosunu giriniz : ')
            rafIndex = input('Rafın indexini giriniz : ') #if else le none veya int cast döndürebilirsin

            rafTur,rafKat,rafNo,rafIndex = req.toCast(rafTur, rafKat, rafNo, rafIndex)
            req.search_record(rafTur, rafKat, rafNo, rafIndex)

        elif choice == '4':
            break

        elif choice == '5':
            req.delPic()



        else:
            print('Invalid input')





# call the main function.
main()
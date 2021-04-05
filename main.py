# encoding:utf-8
import pickle
import req
import string


def main():

    while (True):
        req.show_choices()
        choice = input('Bir seçim yapınız(1-5) : ')
        print()

        if choice == '1':
            req.write_record()
            req.sortPic()

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
            req.delPic()

        elif choice == '5':
            break

        elif choice == '6':
            req.sortPic()



        else:
            print('Invalid input')





# call the main function.
main()
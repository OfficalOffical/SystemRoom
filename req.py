import pickle



def set_data():
    rafTur = str(input('Rafın türünü giriniz : '))
    rafKat = int(input('Rafın katını giriniz : '))
    rafNo = int(input('Rafın Nosunu giriniz : '))
    rafIndex = int(input('Rafın indexini giriniz : '))
    rafIndexData =  input('Rafın datasını giriniz :  ')


    # create a dictionary
    sistem = {}
    sistem['rafTur'] = rafTur
    sistem['rafKat'] = rafKat
    sistem['rafNo'] = rafNo
    sistem['rafIndex'] = rafIndex
    sistem['rafIndexData'] = rafIndexData

    return sistem


def display_data(sistem):
    print('Rafin türü : ', sistem['rafTur'])
    print('Rafin kati : ', sistem['rafKat'])
    print('Rafın No\'su :', sistem['rafNo'])
    print('Rafın Indexi :', sistem['rafIndex'])
    print('Rafın Datası:', sistem['rafIndexData'])
    print()


def write_record():
    # open file in binary mode for writing.
    outfile = open("noSqlDB", 'ab')

    # serialize the object and writing to file
    pickle.dump(set_data(), outfile)

    # close the file
    outfile.close()


def read_records():
    # open file in binary mode for reading
    infile = open('noSqlDB', 'rb')

    # read to the end of file.
    while True:
        try:
            # reading the oject from file
            sistem = pickle.load(infile)

            # display the object
            display_data(sistem)
        except EOFError:
            break

    # close the file
    infile.close()


def search_record(rafTur, rafKat, rafNo, rafIndex):
    infile = open('noSqlDB', 'rb')
    sistem = pickle.load(infile)
    flag = False

    # read to the end of file.
    for x in range((len(sistem)+1)):
        try:

            if (sistem['rafTur'].upper() == rafTur.upper() and rafKat == ""):

                print(sistem['rafTur'],sistem['rafNo'], sistem['rafIndex'], sistem['rafIndexData'])
                flag = True

            elif (sistem['rafTur'].upper() == rafTur.upper() and sistem['rafKat'] == rafKat and
                    rafNo == ""):

                print(sistem['rafNo'], sistem['rafIndex'], sistem['rafIndexData'])
                flag = True

            elif (sistem['rafTur'].upper() == rafTur.upper() and sistem['rafKat'] == rafKat and sistem[
                'rafNo'] == rafNo and rafIndex == ""):

                print(sistem['rafIndex'], sistem['rafIndexData'])
                flag = True

            elif (sistem['rafTur'].upper() == rafTur.upper() and sistem['rafKat'] == rafKat and sistem[
                'rafNo'] == rafNo and sistem['rafIndex'] == rafIndex):

                print(sistem['rafIndexData'])
                flag = True

            sistem = pickle.load(infile)
        except EOFError:
            break

    if flag == False:
        print('Record not Found')
        print()

    # close the file
    infile.close()


def show_choices():
    print('Menü')
    print('1. Kayıt ekle')
    print('2. Bütün kayıtları görüntüle')
    print('3. Spesifik bir kaydı görüntüle')
    print('4. Bir kaydı sil')
    print('5. Çıkış yap')

def toCast(rafTur, rafKat, rafNo, rafIndex):
    if rafTur != "":
        rafTur = str(rafTur) #Change this

    if rafKat != "":
        rafKat = int(rafKat)

    if rafNo != "":
        rafNo = int(rafNo)

    if rafIndex != "":
        rafIndex = int(rafIndex)


    return  rafTur,rafKat,rafNo,rafIndex

def delPic():
    infile = open('noSqlDB', 'rb+')
    sistem = pickle.load(infile)
    flag = False

    rafTur = str(input('Rafın türünü giriniz : '))
    rafKat = int(input('Rafın katını giriniz : '))
    rafNo = int(input('Rafın Nosunu giriniz : '))
    rafIndex = int(input('Rafın indexini giriniz : '))

    # read to the end of file.
    for x in range((len(sistem)+1)):
        try:

            if (sistem['rafTur'].upper() == rafTur.upper() and sistem['rafKat'] == rafKat and sistem['rafNo'] == rafNo and sistem['rafIndex'] == rafIndex):
                print("vololo")
                del  sistem['rafTur'],sistem['rafKat'],sistem['rafNo'],sistem['rafIndex'],sistem['rafIndexData']
                flag = True


        except EOFError:
            break

    if flag == False:
        print('Record not Found')

    infile.close()
# Boli stomac
        p1 = Patient("Pop", "Ioana", "2164567890123", "Obezitate")
        p2 = Patient("Gradinita", "Emilutzbac", "1644567890146", "Obezitate")

        # Boli grave
        p3 = Patient("Baciu", "Tudose", "1246582789345", "Ecoli")
        p4 = Patient("Enigma", "Otiliei", "2647698729365", "Ecoli")
        p5 = Patient("Baciu", "Gheorghe", "2647684529365", "Ecoli")

        # Boli speciale
        p6 = Patient("Baciu", "Aihai", "298784529365", "Febra")
        p7 = Patient("Ion", "Creanga", "2123484529365", "Febra")
        p8 = Patient("Mester", "Pelea", "2123467529365", "Febra")
        p9 = Patient("Garbau", "Opris", "2123484522465", "Durere")

        # Boli psihice
        p10 = Patient("Eminescu", "Mihai", "298784729365", "Schizofrenic")
        p11 = Patient("Pintea", "Vasile", "2123484522365", "Schizofrenic")
        p12 = Patient("Term", "Enescu", "2123466789365", "Febra")
        p13 = Patient("Ulise", "Zeu", "2123412322465", "Durere")

        d1 = Department("Boli stomac", 702, 5, [p1, p2])
        d2 = Department("Boli grave", 100, 3, [p3, p4, p5])
        d3 = Department("Boli speciale", 500, 10, [p6, p7, p8, p9])
        d4 = Department("Boli psihice", 10, 5, [p10, p11, p12, p13])

        self.__prepo.addNew(p1)
        self.__prepo.addNew(p2)
        self.__prepo.addNew(p3)
        self.__prepo.addNew(p4)
        self.__prepo.addNew(p5)
        self.__prepo.addNew(p6)
        self.__prepo.addNew(p7)
        self.__prepo.addNew(p8)
        self.__prepo.addNew(p9)
        self.__prepo.addNew(p10)
        self.__prepo.addNew(p11)
        self.__prepo.addNew(p12)
        self.__prepo.addNew(p13)

        self.__drepo.addNew(d1)
        self.__drepo.addNew(d2)
        self.__drepo.addNew(d3)
        self.__drepo.addNew(d4)
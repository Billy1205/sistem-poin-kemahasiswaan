import pymysql as sql
from pymysql import Error
import tkinter as tk
from tkinter import ttk, messagebox
import tabulate as tbl
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def create_database(database_name):
    global cursor
    try: cursor.execute(f"CREATE DATABASE IF NOT EXISTS {database_name:s};")
    except Error as e: print(f"Error: {e}")
    else: print(f"Database created successfully or already exists: {database_name}")

def use_database(database_name):
    global connection
    try: cursor.execute(f"USE {database_name:s};")
    except Error as e: print(f"Error: {e}")
    else: print(f"Database used: {database_name}")
    
def show_databases():
    global cursor
    try: cursor.execute(f"SHOW DATABASES;")
    except Error as e: print(f"Error: {e}")
    else:
        results = cursor.fetchall()
        print("Databases:")
        for r in results:
            print(*r)

def drop_database(database_name):
    global cursor
    try: cursor.execute(f"DROP DATABASE {database_name:s};")
    except Error as e: print(f"Error: {e}")
    else: print(f"Database dropped: {database_name}")

def create_table(table_name, columns, property=None):
    # format columns: ["col1_name atr1", "col2_name atr2", ...]
    # format property: ["property1", "property2", ...]
    global cursor
    try:
        if property is None:
            cursor.execute(f"CREATE TABLE IF NOT EXISTS {table_name:s} ({', '.join(columns)});")
        else:
            cursor.execute(f"CREATE TABLE IF NOT EXISTS {table_name:s} ({', '.join(columns)}, {', '.join(property)});")
    except Error as e: print(f"Error: {e}")
    else: print(f"Table created successfully or already exists: {table_name}")

def insert_values(table_name, column, values):
    # format column: "col1, col2, col3, ..."
    # format values: [("row1col1", "row1col2"), ("row2col1", "row2col2"), ...]
    global cursor
    try:
        for v in values:
            cursor.execute(f"INSERT INTO {table_name:s} ({column}) VALUES {v};")
    except Error as e: print(f"Error: {e}")
    else: print(f"Value inserted successfully: {len(values)} item(s) into table: {table_name}")

def select_items(type, table_name, property=""):
    # type format: "type1, type2, type3, ..."
    global cursor
    try: cursor.execute(f"SELECT {type} FROM {table_name:s} {property}")
    except Error as e: print(f"Error: {e}")
    else:
        results = cursor.fetchall()
        if len(results) == 0: return
        header = [i[0] for i in cursor.description]
        table = tbl.tabulate(results, header, tablefmt="github")
        # print(table, "\n")
        return [r[0] for r in results] if len(results[0]) == 1 else results, table
    
def update_table(table_name, set, data):
    global cursor
    try: cursor.execute(f"UPDATE {table_name:s} SET {set} WHERE {data};")
    except Error as e: print(f"Error: {e}")
    else: print(f"Table updated successfully: {set} where {data} in table: {table_name}")

def delete_items(table_name, data):
    global cursor
    try: cursor.execute(f"DELETE FROM {table_name:s} WHERE {data};")
    except Error as e: print(f"Error: {e}")
    else: print(f"Items deleted successfully: {data} in table: {table_name}")

def commit():
    global connection
    connection.commit()
    print(f"Transaction saved!")

def connect_mysql(us, pw):
    global connection, cursor
    try:
        connection = sql.connect(
            host="localhost",
            user=us,        
            password=pw,     
            database="company_db", # harap ubah database yang sudah eksis
            charset="utf8mb4"
        )
    except Error as e:
        print(f"Error: {e}")
    else:
        if connection.open:
            print("Connection established")
            cursor = connection.cursor()

def disconnect_mysql():
    global connection, cursor
    try:
        if connection and connection.open:
            cursor.close()
            connection.close()
            print("Connection closed")
        else:
            print("No active connection to close.")
    except Exception as e:
        print(f"Error during disconnection: {e}")
def connect():
    connect_mysql("root", "12345678")
    drop_database("spkDB")
    create_database("spkDB")
    use_database("spkDB")
    create_table("mahasiswa", ["id VARCHAR(16) PRIMARY KEY",
                               "password VARCHAR(32)",
                               "name VARCHAR(200)",
                               "major VARCHAR(100)",
                               "email VARCHAR(100)",
                               "phone_number VARCHAR(20)",
                               "enrollment_year INT",
                               "points_earned DECIMAL(4, 2)"])
    insert_values("mahasiswa", "id,password,name,major,email,phone_number,enrollment_year,points_earned",
                               [("1","1","Dono Kasi Know","SCCE","email@email.com","0897894",2021,0.00)])
    insert_values("mahasiswa", "id,password,name,major,email,phone_number,enrollment_year,points_earned",
                               [(232000602, 232000602, "Kenneth Edson Wijaya", "SCCE", "kwijaya02@students.calvin.ac.id", "085173025040", 2023, 0.00), (232102206, 232102206, "Howell Deevan Gunawan", "IBDA", "hgunawan06@students.calvin.ac.id", "089626703989", 2023, 0.00), (232102230, 232102230, "Watson Lim", "BMS", "wlim30@students.calvin.ac.id", "088214461520", 2023, 0.00), (232102253, 232102253, "Jeneva Daniella", "ASD", "jdaniella53@students.calvin.ac.id", "081310881079", 2023, 0.00), (232102309, 232102309, "Felicia Calista", "IBDA", "fcalista09@students.calvin.ac.id", "082123622107", 2023, 0.00), (232102317, 232102317, "Philemon", "IBDA", "pphilemon17@students.calvin.ac.id", "082346327919", 2023, 0.00), (232200137, 232200137, "Calvin Jonathan Djulianus", "BMS", "cdjulianus37@students.calvin.ac.id", "085215921002", 2023, 0.00), (232200155, 232200155, "Jeremy Matthew Ramon Rumendong", "IEE", "jrumendong55@students.calvin.ac.id", "082195071477", 2023, 0.00), (232200156, 232200156, "Alfandi Wijaya", "IBDA", "awijaya56@students.calvin.ac.id", "089507013965", 2023, 0.00), (232200169, 232200169, "Kezia Rambu Durry", "CFP", "kdurry69@students.calvin.ac.id", "082191541800", 2023, 0.00), (232200183, 232200183, "Calvin James Riyono", "IEE", "criyono83@students.calvin.ac.id", "081236503435", 2023, 0.00), (232200245, 232200245, "Xander Alvaro Tjan", "IBDA", "xtjan45@students.calvin.ac.id", "082210739775", 2023, 0.00), (232200346, 232200346, "Alvern Brainard", "IBDA", "abrainard46@students.calvin.ac.id", "087808275119", 2023, 0.00), (232200410, 232200410, "Laurentius Santiago Pratama", "IBDA", "lpratama10@students.calvin.ac.id", "0895395682551", 2023, 0.00), (232200417, 232200417, "Zavier Abbel Christian", "IEE", "zchristian17@students.calvin.ac.id", "081216501974", 2023, 0.00), (232201332, 232201332, "Shindy Estera", "IBDA", "sestera32@students.calvin.ac.id", "082310918563", 2023, 0.00), (232201765, 232201765, "Nick Olvan", "ASD", "nolvan65@students.calvin.ac.id", "0818472616", 2023, 0.00), (232201993, 232201993, "Miracle Ila Willymarsa", "BMS", "mwillymarsa93@students.calvin.ac.id", "", 2023, 0.00), (232202160, 232202160, "Michael Bryan Pontoh Aalang", "BMS", "maalang60@students.calvin.ac.id", "085242805904", 2023, 0.00), (232202177, 232202177, "Grace Devina Romauli Hutapea", "IBDA", "ghutapea77@students.calvin.ac.id", "081243108382", 2023, 0.00), (232202462, 232202462, "Reuben Zachary Susanto", "IBDA", "rsusanto62@students.calvin.ac.id", "08118495021", 2023, 0.00), (232202699, 232202699, "Vonny Christy Lim", "ASD", "vlim99@students.calvin.ac.id", "081213399927", 2023, 0.00), (232202718, 232202718, "Elicia Gloria Tirtajaya Budiawan", "CFP", "ebudiawan18@students.calvin.ac.id", "087880045650", 2023, 0.00), (232202858, 232202858, "Elvio Trixie", "BMS", "etrixie58@students.calvin.ac.id", "082310710995", 2023, 0.00), (232202903, 232202903, "Nadine Angelica Subrata", "BMS", "nsubrata03@students.calvin.ac.id", "087820060201", 2023, 0.00), (232202911, 232202911, "Manuel Togi", "IBDA", "mtogi11@students.calvin.ac.id", "081218561951", 2023, 0.00), (232202935, 232202935, "Devlin Manuel", "IBDA", "dmanuel35@students.calvin.ac.id", "0895605248875", 2023, 0.00), (232202943, 232202943, "Dave Sean Tjundawan", "ASD", "dtjundawan43@students.calvin.ac.id", "081395952080", 2023, 0.00), (232202944, 232202944, "Jovanca Kenes Lie", "BMS", "jlie44@students.calvin.ac.id", "081285301451", 2023, 0.00), (232202959, 232202959, "Billy Hartono", "IBDA", "bhartono59@students.calvin.ac.id", "085887988806", 2023, 0.00), (232202970, 232202970, "Aprinda Kornelius Hanson", "IEE", "ahanson70@students.calvin.ac.id", "082273507558", 2023, 0.00), (232202983, 232202983, "Brian Christian Suroso", "IBDA", "bsuroso83@students.calvin.ac.id", "085156829865", 2023, 0.00), (232202993, 232202993, "Jessie Jeyenette Prolifience Simamora", "CFP", "jsimamora93@students.calvin.ac.id", "087803562904", 2023, 0.00), (232203010, 232203010, "Joshua Anthony Kwik", "IEE", "jkwik10@students.calvin.ac.id", "085262268257", 2023, 0.00), (232203016, 232203016, "Frits Aloy Sius Jamie Silalahi", "IEE", "fsilalahi16@students.calvin.ac.id", "08811343530", 2023, 0.00), (232203050, 232203050, "Oland Gifto Paembonan", "BMS", "opaembonan50@students.calvin.ac.id", "082128523848", 2023, 0.00), (232203057, 232203057, "Dhetya Octaviani Melstain", "CFP", "dmelstain57@students.calvin.ac.id", "082291599619", 2023, 0.00), (232203068, 232203068, "Matthew Layadi", "IBDA", "mlayadi68@students.calvin.ac.id", "085781018483", 2023, 0.00), (232203079, 232203079, "Ivena Claresta Cong Lady", "BMS", "ilady79@students.calvin.ac.id", "081398175257", 2023, 0.00), (232203080, 232203080, "Caroline Huka", "CFP", "chuka80@students.calvin.ac.id", "081228286795", 2023, 0.00), (232203081, 232203081, "Patrick Kent", "CFP", "pkent81@students.calvin.ac.id", "081281138545", 2023, 0.00), (232203082, 232203082, "Praisilia Miracle Parengka", "ASD", "pparengka82@students.calvin.ac.id", "081360660009", 2023, 0.00), (232203088, 232203088, "Timotius", "IBDA", "ttimotius88@students.calvin.ac.id", "0895705011300", 2023, 0.00), (232203102, 232203102, "Stephanus Mikhael", "ASD", "smikhael02@students.calvin.ac.id", "0895365788277", 2023, 0.00), (232203115, 232203115, "Marniwati Waruwu", "IEE", "mwaruwu15@students.calvin.ac.id", "081379088623", 2023, 0.00), (232203131, 232203131, "Yoyada Rava Christiana Harun", "IBDA", "yharun31@students.calvin.ac.id", "085363093322", 2023, 0.00), (232203147, 232203147, "Albert Santoso", "ASD", "asantoso47@students.calvin.ac.id", "085212349301", 2023, 0.00), (232203155, 232203155, "Darren Nathaniel Hendra", "SCCE", "dhendra55@students.calvin.ac.id", "081257265140", 2023, 0.00), (232203163, 232203163, "Serlin Antonia Utomo", "BMS", "sutomo63@students.calvin.ac.id", "082184000688", 2023, 0.00), (232203170, 232203170, "Theophilus Santoso", "IEE", "tsantoso70@students.calvin.ac.id", "081215003500", 2023, 0.00), (232203173, 232203173, "Stiven Lee", "IBDA", "slee73@students.calvin.ac.id", "089602755448", 2023, 0.00), (232203185, 232203185, "Arnold Santoso", "SCCE", "asantoso85@students.calvin.ac.id", "085212349287", 2023, 0.00), (232203197, 232203197, "Yosafat Rohan Ariyanto", "IEE", "yariyanto97@students.calvin.ac.id", "082193394813", 2023, 0.00), (232203201, 232203201, "Henri Rusmanto", "CFP", "hrusmanto01@students.calvin.ac.id", "081281203996", 2023, 0.00), (232203202, 232203202, "Kefas Misael Jireh", "CFP", "kjireh02@students.calvin.ac.id", "085880164942", 2023, 0.00), (232203204, 232203204, "William Cong Putra", "BMS", "wputra04@students.calvin.ac.id", "081219717128", 2023, 0.00), (232203209, 232203209, "Valerie Novis Josephine", "CFP", "vjosephine09@students.calvin.ac.id", "082124470166", 2023, 0.00), (232203229, 232203229, "Joles Lin", "IBDA", "jlin29@students.calvin.ac.id", "0897 9001 063 ", 2023, 0.00), (232203245, 232203245, "Joey Victor Natanael Djaja", "IBDA", "jdjaja45@students.calvin.ac.id", "082147408816", 2023, 0.00), (232203269, 232203269, "William Christian Diputra", "IEE", "wdiputra69@students.calvin.ac.id", "08113987777", 2023, 0.00), (232203468, 232203468, "Grace Ellen", "IBDA", "gellen68@students.calvin.ac.id", "0895364573972", 2023, 0.00), (232203527, 232203527, "Albern Carlen Daniswara", "IBDA", "adaniswara27@students.calvin.ac.id", "087851242435", 2023, 0.00), (232203558, 232203558, "Clara Maria Lie", "IBDA", "clie58@students.calvin.ac.id", "087709238755", 2023, 0.00), (232203579, 232203579, "Shendy Abraham", "CFP", "sabraham79@students.calvin.ac.id", "081240566198", 2023, 0.00), (232203581, 232203581, "Marchelia Aurel Samantha", "CFP", "msamantha81@students.calvin.ac.id", "082125522363", 2023, 0.00), (232203585, 232203585, "Bait Stefanus Marpaung", "SCCE", "bmarpaung85@students.calvin.ac.id", "081337805010", 2023, 0.00), (232203595, 232203595, "Rendi Anferta", "IBDA", "ranferta95@students.calvin.ac.id", "087740348431", 2023, 0.00), (232203596, 232203596, "Moreno Rafael Limanu", "SCCE", "mlimanu96@students.calvin.ac.id", "082189957377", 2023, 0.00), (232203597, 232203597, "Wilzes Marcello Tan", "IBDA", "wtan97@students.calvin.ac.id", "087825737248", 2023, 0.00), (232300101, 232300101, "Shem Ferdinand", "SCCE", "sferdinand01@students.calvin.ac.id", "081919181819", 2023, 0.00), (232300107, 232300107, "Ni Ketut Widiani", "BMS", "nwidiani07@students.calvin.ac.id", "083813910710", 2023, 0.00), (232300115, 232300115, "Petra Gamma Setya Agatha", "IBDA", "pagatha15@students.calvin.ac.id", "085712632150", 2023, 0.00), (232300116, 232300116, "Clarissa Aurelia Kirana", "ASD", "ckirana16@students.calvin.ac.id", "082279989899", 2023, 0.00), (232300125, 232300125, "Paulina Devina Wijaya", "IBDA", "pwijaya25@students.calvin.ac.id", "087865935124", 2023, 0.00), (232300137, 232300137, "Niel Christian Jonathan", "IBDA", "njonathan37@students.calvin.ac.id", "081717612935", 2023, 0.00), (232300254, 232300254, "Hana Guwanto", "IBDA", "hguwanto54@students.calvin.ac.id", "085975274010", 2023, 0.00), (232300289, 232300289, "Ema Nelvi Saleky", "IBDA", "esaleky89@students.calvin.ac.id", "082197600157", 2023, 0.00), (232300297, 232300297, "Stefani Tania", "BMS", "stania97@students.calvin.ac.id", "081385258008", 2023, 0.00), (232300333, 232300333, "Naftali Aditya Agung Dwi Nugraha", "IBDA", "nnugraha33@students.calvin.ac.id", "08819776289", 2023, 0.00), (232300338, 232300338, "Nicholas Ian Rusli", "BMS", "nrusli38@students.calvin.ac.id", "085883100980", 2023, 0.00), (232300422, 232300422, "Angelika Sabrina Simamora", "SCCE", "asimamora22@students.calvin.ac.id", "083120540849", 2023, 0.00), (232300425, 232300425, "Angela Thenu", "ASD", "athenu25@students.calvin.ac.id", "081262157569", 2023, 0.00), (232300500, 232300500, "Chrisustomus Boimau", "IBDA", "cboimau00@students.calvin.ac.id", "081218198570", 2023, 0.00), (232300676, 232300676, "Stephen Moses Lumbanradja", "IBDA", "slumbanradja76@students.calvin.ac.id", "08111999459", 2023, 0.00), (232300935, 232300935, "Grace Tedjokusumo", "CFP", "gtedjokusumo35@students.calvin.ac.id", "085777999531", 2023, 0.00), (232301019, 232301019, "Makarios Pardamean Manurung", "IBDA", "mmanurung19@students.calvin.ac.id", "081297998532", 2023, 0.00), (232301226, 232301226, "Keanrich Cordana", "IBDA", "kcordana26@students.calvin.ac.id", "081352794189", 2023, 0.00), (232301421, 232301421, "Armand Crystoffer Tambunan", "IEE", "atambunan21@students.calvin.ac.id", "081802106601", 2023, 0.00)])
    create_table("staff", ["id VARCHAR(16) PRIMARY KEY",
                           "password VARCHAR(32)",
                           "name VARCHAR(200)",
                           "position VARCHAR(100)",
                           "email VARCHAR(100)",
                           "phone_number VARCHAR(20)",
                           "joining_date VARCHAR(10)"])
    insert_values("staff", "id,password,name,position,email,phone_number,joining_date",
                           [("11","11","Michael Andrew","Computer Science","michael.andrews@example.com","081234567890","3-12-2020")])
    insert_values("staff", "id,password,name,position,email,phone_number,joining_date",
                           [(20170001, 20170001, "Adhya Kumara", "SCCE", "adhya.kumara@calvin.ac.id", "081234567890", "01-01-2017"), (20170002, 20170002, "Aditya Heru Prathama", "IEE", "aditya.prathama@calvin.ac.id", "081234567890", "01-01-2017"), (20170003, 20170003, "Agung Bayu Waluyo", "Rektorat", "agung.waluyo@calvin.ac.id", "081234567890", "01-01-2017"), (20170004, 20170004, "Azalia Yisrael Ie", "ASD", "azalia.yisrael@calvin.ac.id", "081234567890", "01-01-2017"), (20170005, 20170005, "Bambang Loreno", "EMI", "bambang.loreno@calvin.ac.id", "081234567890", "01-01-2017"), (20170006, 20170006, "Budi Chang", "IBDA", "budi.chang@calvin.ac.id", "081234567890", "01-01-2017"), (20170007, 20170007, "Clarence Amadeus", "IEE", "clarence.amadeus@calvin.ac.id", "081234567890", "01-01-2017"), (20170008, 20170008, "Clarissa Theophilia", "Other", "clarissa.theophilia@calvin.ac.id", "081234567890", "01-01-2017"), (20170009, 20170009, "Dadang Suryana", "SD", "dadang.suryana@calvin.ac.id", "081234567890", "01-01-2017"), (20170010, 20170010, "David Tong", "Rektorat", "david.tong@calvin.ac.id", "081234567890", "01-01-2017"), (20170011, 20170011, "Dicky Susanto", "GL", "dicky.susanto@calvin.ac.id", "081234567890", "01-01-2017"), (20170012, 20170012, "Edvan Arifsaputra Suherman", "BMS", "edvan.suherman@calvin.ac.id", "081234567890", "01-01-2017"), (20170013, 20170013, "Elda Alderin", "CR", "elda.alderin@calvin.ac.id", "081234567890", "01-01-2017"), (20170014, 20170014, "Emajanti", "CR", "emajanti@calvin.ac.id", "081234567890", "01-01-2017"), (20170015, 20170015, "Enji", "CR", "enji@calvin.ac.id", "081234567890", "01-01-2017"), (20170016, 20170016, "Erwan Zhang", "GL", "erwan.zhang@calvin.ac.id", "081234567890", "01-01-2017"), (20170017, 20170017, "Erwin A. Tumengkol", "EMI", "erwin.tumengkol@calvin.ac.id", "081234567890", "01-01-2017"), (20170018, 20170018, "Erwin Anggadjaja", "IBDA", "erwin.anggadjaja@calvin.ac.id", "081234567890", "01-01-2017"), (20170019, 20170019, "Esther Dorothy Nabasa Sinaga", "ASD", "esther.dorothy@calvin.ac.id", "081234567890", "01-01-2017"), (20170020, 20170020, "Ezra Yoanes Setiasabda Tjung", "SCCE", "ezra.tjung@calvin.ac.id", "081234567890", "01-01-2017"), (20170021, 20170021, "Fini Angela Perangin-Angin", "DBI", "fini.angela@calvin.ac.id", "081234567890", "01-01-2017"), (20170022, 20170022, "Fritz Harland Sihombing", "SCCE", "fritz.sihombing@calvin.ac.id", "081234567890", "01-01-2017"), (20170023, 20170023, "Ghandy Salim", "IBDA", "ghandy.salim@calvin.ac.id", "081234567890", "01-01-2017"), (20170024, 20170024, "Giovania Evangeline Halim", "CFP", "giovania.halim@calvin.ac.id", "081234567890", "01-01-2017"), (20170025, 20170025, "Giska Raissa", "ASD", "giska.raissa@calvin.ac.id", "081234567890", "01-01-2017"), (20170026, 20170026, "Hartiyowidi Yuliawuri", "BMS", "hartiyowidi.yuliawuri@calvin.ac.id", "081234567890", "01-01-2017"), (20170027, 20170027, "Harwin", "CFP", "harwin@calvin.ac.id", "081234567890", "01-01-2017"), (20170028, 20170028, "Hendrik Santoso Sugiarto", "IBDA", "hendrik.sugiarto@calvin.ac.id", "081234567890", "01-01-2017"), (20170029, 20170029, "I Nyoman Wirasena", "VSC", ".wirasena@calvin.ac.id", "081234567890", "01-01-2017"), (20170030, 20170030, "Ira Petri Hutabarat", "Staff", "ira.petri@calvin.ac.id", "081234567890", "01-01-2017"), (20170031, 20170031, "Ivan A. Abednego", "ASD", "ivan.abednego@calvin.ac.id", "081234567890", "01-01-2017"), (20170032, 20170032, "Jadi Sampurna Lima", "GL", "jadi.lima@calvin.ac.id", "081234567890", "01-01-2017"), (20170033, 20170033, "Jayandi Soriasi Panggabean", "IEE", "jayandi.panggabean@calvin.ac.id", "081234567890", "01-01-2017"), (20170034, 20170034, "Jeffrey Wibowo", "Discipleship", "jeffrey.wibowo@calvin.ac.id", "081234567890", "01-01-2017"), (20170035, 20170035, "Jerry Jonathan Zebua", "CR", "jerry.zebua@calvin.ac.id", "081234567890", "01-01-2017"), (20170036, 20170036, "Kelly K. Audrey", "IBDA", "kelly.audrey@calvin.ac.id", "081234567890", "01-01-2017"), (20170037, 20170037, "Kevin Kusnadi", "BMS", "kevin.kusnadi@calvin.ac.id", "081234567890", "01-01-2017"), (20170038, 20170038, "Lili Mesak", "BMS", "lili.mesak@calvin.ac.id", "081234567890", "01-01-2017"), (20170039, 20170039, "Lucia Kusumawati", "BMS", "lucia.kusumawati@calvin.ac.id", "081234567890", "01-01-2017"), (20170040, 20170040, "Margaretha Serevina", "Library", "margaretha.serevina@calvin.ac.id", "081234567890", "01-01-2017"), (20170041, 20170041, "Maria Anindita Nauli", "CFP", "maria.nauli@calvin.ac.id", "081234567890", "01-01-2017"), (20170042, 20170042, "Martin Tjahjono", "Rektorat", "martin.tjahjono@calvin.ac.id", "081234567890", "01-01-2017"), (20170043, 20170043, "Melani Kowureng", "SAS", "melani.kowureng@calvin.ac.id", "081234567890", "01-01-2017"), (20170044, 20170044, "Meta Chandra", "Konselor", "meta.chandra@calvin.ac.id", "081234567890", "01-01-2017"), (20170045, 20170045, "Meyland", "SCCE", "meyland@calvin.ac.id", "081234567890", "01-01-2017"), (20170046, 20170046, "Nathanael Steven Wong", "BMS", "nathanael.wong@calvin.ac.id", "081234567890", "01-01-2017"), (20170047, 20170047, "Nathania Wijaya", "ASD", "nathania.wijaya@calvin.ac.id", "081234567890", "01-01-2017"), (20170048, 20170048, "Pasu Silaban", "Library", "pasu.silaban@calvin.ac.id", "081234567890", "01-01-2017"), (20170049, 20170049, "Pilandari Lembono", "BMS", "pilandari.lembono@calvin.ac.id", "081234567890", "01-01-2017"), (20170050, 20170050, "Rere", "CR", "rere@calvin.ac.id", "081234567890", "01-01-2017"), (20170051, 20170051, "Samuel Pangeran", "CFP", "samuel.pangeran@calvin.ac.id", "081234567890", "01-01-2017"), (20170052, 20170052, "Sanga Lawalata", "IBDA", "sanga.lawalata@calvin.ac.id", "081234567890", "01-01-2017"), (20170053, 20170053, "Santa Monica Tambunan", "CR", "santa.monica@calvin.ac.id", "081234567890", "01-01-2017"), (20170054, 20170054, "Santina Sipayung", "SCCE", "santina.sipayung@calvin.ac.id", "081234567890", "01-01-2017"), (20170055, 20170055, "Stephanus Sahala Hutagalung", "GA", "stephanus.sahala@calvin.ac.id", "081234567890", "01-01-2017"), (20170056, 20170056, "Stephen Bennardy", "Discipleship", "stephen.bennardy@calvin.ac.id", "081234567890", "01-01-2017"), (20170057, 20170057, "Steven Bandong", "IBDA", "steven.bandong@calvin.ac.id", "081234567890", "01-01-2017"), (20170058, 20170058, "Sukadarminto", "SCCE", "sukadarminto@calvin.ac.id", "081234567890", "01-01-2017"), (20170059, 20170059, "Tatit Kurniasih", "EMI", "tatit.kurniasih@calvin.ac.id", "081234567890", "01-01-2017"), (20170060, 20170060, "Timur Pratama Wiradarma", "GL", "timur.wiradarma@calvin.ac.id", "081234567890", "01-01-2017"), (20170061, 20170061, "Valentino Sitorus", "Discipleship", "valentino.sitorus@calvin.ac.id", "081234567890", "01-01-2017"), (20170062, 20170062, "Victor Chris Samuel Purba", "IBDA", "victor.purba@calvin.ac.id", "081234567890", "01-01-2017"), (20170063, 20170063, "Vincent Wiguna", "GL", "vincent.wiguna@calvin.ac.id", "081234567890", "01-01-2017"), (20170064, 20170064, "Virginia Lalujan", "EMI", "virginia.lalujan@calvin.ac.id", "081234567890", "01-01-2017"), (20170065, 20170065, "Wilham G. Louhenapessy", "SCCE", "wilham.louhenapessy@calvin.ac.id", "081234567890", "01-01-2017"), (20170066, 20170066, "Yozef Giovanni Tjandra", "IBDA", "yozef.tjandra@calvin.ac.id", "081234567890", "01-01-2017")])
    create_table("events", ["id VARCHAR(16) PRIMARY KEY",
                            "name VARCHAR(200)",
                            "status VARCHAR(15)",
                            "category VARCHAR(50)",
                            "speaker VARCHAR(200)",
                            "date VARCHAR(10)",
                            "time VARCHAR(5)",
                            "point DECIMAL(4, 2)",
                            "max_repetition INT"])
    insert_values("events", "id,name,status,category,speaker,date,time,point,max_repetition",
                           [("SPIKA6", "SPIK: Manusia VI", "available", "Seminar", "Pdt. Stephen Tong", "24-08-2024", "09:00", 0.25, 6), ("SPIKE1", "SPIK: Gereja I", "available", "Seminar", "Pdt. Stephen Tong", "02-11-2024", "09:00", 0.25, 6), ("DN6", "Dies Natalis VI", "available", "Akademik", "Pdt. David Tong", "30-11-2024", "14:00", 0.25, 1), ("CMY2024", "Commencement Year 2024", "available", "Akademik", "Pdt. David Tong", "23-08-2024", "14:00", 0.25, 1), ("PBK2425", "Ibadah Convocation Tahun Akademik CIT 2024/2025", "available", "Akademik", "Pdt. David Tong", "21-08-2024", "10:00", 0.2, 1), ("UP17A24", "Upacara 17 Agustus", "available", "Akademik", "Pdt. David Tong", "17-08-2024", "10:00", 0.2, 1), ("HSK2024", "Hari Cinta Kampus", "available", "Non-Akademik", "Student Organization", "29-10-2024", "13:00", 0.15, 1), ("OH2024", "Open House", "available", "Non-Akademik", "Communication and Relations", "30-08-2024", "08:00", 0.15, 1), ("BEMTH", "BEM Townhall", "available", "Non-Akademik", "Student Organization", "27-09-2024", "13:00", 0.15, 5), ("SD01", "Sosialisasi dan Talkshow SD: Pengembangan Prestasi Mahasiswa", "available", "Workshop", "Martin Tjahjono", "20-11-2024", "13:00", 0.2, 5), ("STT04", "STT: Doa Imam Besar", "available", "Seminar", "Prof. Peter Lillback", "19-11-2024", "19:00", 0.25, 6), ("STT03", "STT: Bagaimana Seharusnya Orang Kristen Memandang Israel Modern: dari Berdirinya hingga Isu Perang Terkini", "available", "Seminar", "Rev. Benny Lee, M.Div., M.A.", "12-11-2024", "19:00", 0.25, 6), ("STT02", "STT: Konsili Nicea", "available", "Seminar", "Prof. Herman Selderhuis", "22-10-2024", "19:00", 0.25, 6), ("SD02", "Knowing Yourself: Stress, Depression, Bipolar?", "available", "Workshop", "Meta Chandra", "23-11-2024", "10:00", 0.2, 5), ("STT01", "STT: Siapkah Anda menghadapi Antitesis?", "available", "Seminar", "Prof. Richard Pratt", "17-09-2024", "19:00", 0.25, 6), ("ASJ01", "Oratorio Month: Haydn The Creation", "available", "Konser", "Pdt. Stephen Tong", "5-10-2024", "17:00", 0.25, 5), ("ASJ02", "Oratorio Month: Mendelssohn Elijah", "available", "Konser", "Pdt. Stephen Tong", "12-10-2024", "17:00", 0.25, 5), ("ASJ03", "Oratorio Month: Handel Messiah", "available", "Konser", "Pdt. Stephen Tong", "19-10-2024", "17:00", 0.25, 5), ("ASJ04", "Oratorio Month: Haydn The Seasons, Mendelssohn Lobgesang", "available", "Konser", "Pdt. Stephen Tong", "26-10-2024", "17:00", 0.25, 5), ("ASJ05", "Light Ministry Orchestra", "available", "Konser", "Addie M. S.", "3-11-2024", "17:00", 0.25, 5), ("CMS01", "CMS of ASJ: Voice and Piano", "available", "Konser", "Jessica Januar, Edith Widayani", "6-11-2024", "17:00", 0.25, 5), ("ASJ06", "Jakarta Festival Chorus", "available", "Konser", "Vincent Wiguna", "9-11-2024", "17:00", 0.25, 5), ("ASJ07", "Yayasan Musik Amadeus Indonesia", "available", "Konser", "Amadeus Symphony Orchestra", "16-11-2024", "17:00", 0.25, 5), ("ASJ08", "JSO: Rachmaninoff Piano Concerto No. 3", "available", "Konser", "Jahja Ling", "23-11-2024", "17:00", 0.25, 5), ("ASJ09", "JSO: Family Concert", "available", "Konser", "Eunice Tong", "1-12-2024", "17:00", 0.25, 5), ("ASJ10", "JSO & JOS: Christmas Concerts I", "available", "Konser", "Eunice Tong", "14-12-2024", "17:00", 0.25, 5), ("ASJ11", "JSO & JOS: Christmas Concerts II", "available", "Konser", "Eunice Tong", "15-12-2024", "17:00", 0.25, 5), ("IBDA01", "Prodi Gathering", "available", "HIMA", "HIMA", "30-11-2024", "14:00", 0.15, 5)])
    create_table("log_mahasiswa", ["id_mahasiswa VARCHAR(16)",
                                   "id_event VARCHAR(16)"],
                                  ["FOREIGN KEY (id_mahasiswa) REFERENCES mahasiswa(id) ON DELETE RESTRICT",
                                   "FOREIGN KEY (id_event) REFERENCES events(id) ON DELETE RESTRICT"])
    insert_values("log_mahasiswa", "id_mahasiswa, id_event",
                                   [("232203081","DN6"), ("232203082","DN6"), ("232203088","DN6"), ("232203102","DN6"), ("232203115","DN6"), ("232203131","DN6"), ("232203147","DN6"), ("232203155","DN6"), ("232203163","DN6"), ("232203170","DN6"), ("232203173","DN6"), ("232203185","DN6"), ("232203197","DN6"), ("232203201","DN6"), ("232203202","DN6"), ("232203204","DN6"), ("232203209","DN6"), ("232203229","DN6"), ("232203245","DN6"), ("232203269","DN6"), ("232203468","DN6"), ("232203527","DN6"), ("232203558","DN6"), ("232203579","DN6"), ("232203581","DN6"), ("232203585","DN6"), ("232203595","DN6"), ("232203596","DN6"), ("232203597","DN6"), ("232300101","DN6"), ("232300107","DN6"), ("232300115","DN6"), ("232300116","DN6"), ("232300125","DN6"), ("232300137","DN6"), ("232300254","DN6"), ("232300289","DN6"), ("232300297","DN6"), ("232300333","DN6"), ("232300338","DN6"), ("232300422","DN6"), ("232300425","DN6"), ("232300500","DN6"), ("232300676","DN6"), ("232300935","DN6"), ("232301019","DN6"), ("232301226","DN6"), ("232301421","DN6")])
    create_table("log_staff", ["id_staff VARCHAR(16)",
                               "id_event VARCHAR(16)"],
                               ["FOREIGN KEY (id_staff) REFERENCES staff(id) ON DELETE RESTRICT",
                               "FOREIGN KEY (id_event) REFERENCES events(id) ON DELETE RESTRICT"])
    insert_values("log_staff", "id_staff, id_event",
                                   [("20170009","DN6"), ("20170010","DN6"), ("20170011","DN6"), ("20170012","DN6"), ("20170013","DN6"), ("20170014","DN6"), ("20170015","DN6"), ("20170016","DN6"), ("20170017","DN6"), ("20170018","DN6"), ("20170019","DN6"), ("20170020","DN6"), ("20170021","DN6"), ("20170022","DN6"), ("20170023","DN6"), ("20170024","DN6"), ("20170025","DN6"), ("20170026","DN6"), ("20170027","DN6"), ("20170028","DN6"), ("20170029","DN6"), ("20170030","DN6"), ("20170031","DN6"), ("20170032","DN6"), ("20170033","DN6"), ("20170034","DN6"), ("20170035","DN6"), ("20170036","DN6"), ("20170037","DN6"), ("20170038","DN6"), ("20170039","DN6"), ("20170040","DN6"), ("20170041","DN6"), ("20170042","DN6"), ("20170043","DN6"), ("20170044","DN6"), ("20170045","DN6"), ("20170046","DN6"), ("20170047","DN6"), ("20170048","DN6"), ("20170049","DN6"), ("20170050","DN6"), ("20170051","DN6"), ("20170052","DN6"), ("20170053","DN6"), ("20170054","DN6"), ("20170055","DN6"), ("20170056","DN6"), ("20170057","DN6"), ("20170058","DN6"), ("20170059","DN6"), ("20170060","DN6"), ("20170061","DN6"), ("20170062","DN6"), ("20170063","DN6")])

""""""""""""""""""

def show_frame(name):
    frames = {"login":frame_login, "student":frame_student, "staff":frame_staff, "admin":frame_admin, "show_events":frame_show_events, "new_events":frame_new_events, "show_students":frame_show_students, "new_students":frame_new_students, "show_staffs":frame_show_staffs, "new_staff":frame_new_staffs, "check_attendance":frame_check_attendance}
    for f in frames.values():
        f.grid_forget()
    frame = frames[name]
    frame.grid(row=0, column=0, sticky="nsew")
    if name == 'student':
        student_profile()
    elif name == 'staff':
        staff_profile()
    elif name == 'login':
        frame_login_entry_username.delete(0, tk.END)
        frame_login_entry_password.delete(0, tk.END)
    elif name == 'show_students':
        list_box_students()
        load_all_data_students()
    elif name == 'show_staff':
        list_box_staffs()
        load_all_data_staffs()
    frame.tkraise()

connect()
root = tk.Tk()
root.title('Aplikasi SPK')
root.geometry('900x600')
# root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

frame_login = ttk.Frame(root)
frame_student = ttk.Frame(root)
frame_staff = ttk.Frame(root)
frame_admin = ttk.Frame(root)
frame_show_events = ttk.Frame(root)
frame_new_events = ttk.Frame(root)
frame_show_students = ttk.Frame(root)
frame_new_students = ttk.Frame(root)
frame_show_staffs = ttk.Frame(root)
frame_new_staffs = ttk.Frame(root)
frame_check_attendance = ttk.Frame(root)

for frame in (frame_login, frame_student, frame_staff, frame_admin, frame_show_events, frame_new_events, frame_show_students, frame_new_students, frame_show_staffs, frame_new_staffs, frame_check_attendance):
    frame.grid()


""" Frame Login """
def login_validation(username, password):
    if username in adminD and password == adminD[username]:
        frame_login_label_result.config(text="Login berhasil sebagai admin", foreground="green", justify="center")
        frame_login_label_result.config(text="")
        show_frame('admin')
    elif username in (student := {s[0]:s[1] for s in select_items("id, password", "mahasiswa")[0]}) and password == student[username]:
        frame_login_label_result.config(text="Login berhasil sebagai mahasiswa", foreground="green", justify="center")
        frame_login_label_result.config(text="")
        show_frame('student')
        load_all_data_events_students()
    elif username in (staff := {s[0]:s[1] for s in select_items("id, password", "staff")[0]}) and password == staff[username]:
        frame_login_label_result.config(text="Login berhasil sebagai staff", foreground="green", justify="center")
        frame_login_label_result.config(text="")
        load_all_data_events_staffs()
        show_frame('staff')
    else:
        frame_login_label_result.config(text="Login gagal. Username atau password salah.", foreground="red", justify="center")
    
frame_login_label = ttk.LabelFrame(frame_login, text='SPK')
frame_login_label.grid(row=0, column=0, columnspan=2, padx=5, pady=5)
frame_login_label_username = ttk.Label(frame_login_label, text="Username:")
frame_login_label_username.grid(row=0, column=0, padx=5, pady=5)
frame_login_entry_username = ttk.Entry(frame_login_label)
frame_login_entry_username.grid(row=0, column=1, padx=5, pady=5)
frame_login_label_password = ttk.Label(frame_login_label, text="Password:")
frame_login_label_password.grid(row=1, column=0, padx=5, pady=5)
frame_login_entry_password = ttk.Entry(frame_login_label, show="*")
frame_login_entry_password.grid(row=1, column=1, padx=5, pady=5)

frame_login_label_result = ttk.Label(frame_login, text="", foreground="red", justify="center")
frame_login_label_result.grid(row=2, column=0, columnspan=2, pady=5)
frame_login_button_submit = ttk.Button(frame_login, text='Submit', command=lambda: login_validation(frame_login_entry_username.get(), frame_login_entry_password.get()))
frame_login_button_submit.grid(row=3, column=0, columnspan=2, pady=5)
frame_login.grid_columnconfigure(0, weight=1)
# frame_login.grid_columnconfigure(1, weight=1)


""" Frame Students """ 
def create_profile_page(root, profile_data, labels, row, col):
    # Frame untuk menampung seluruh konten
    frame = tk.Frame(root, padx=20, pady=20)
    frame.grid(row=row, column=col, columnspan=2, sticky='w')

    # Header
    header = tk.Label(frame, text="Profile", font=("Helvetica", 10, "bold"))
    header.grid(row=0, column=0, columnspan=2, pady=10)

    # Loop untuk membuat label dan data secara dinamis
    for i, (label, value) in enumerate(zip(labels, profile_data)):
        # Label untuk tiap data
        label_widget = tk.Label(frame, text=f"{label}:", font=("Helvetica", 10), anchor="w")
        label_widget.grid(row=i + 1, column=0, sticky="w", padx=10,)
        
        # Nilai untuk tiap data
        value_widget = tk.Label(frame, text=value, font=("Helvetica", 10), anchor="w")
        value_widget.grid(row=i + 1, column=1, sticky="w", padx=10)

def student_profile():
    student_id = frame_login_entry_username.get()
    header_student_profile = ['Id', 'Password', 'Nama', 'Prodi', 'Email', 'Nomor Kontak', 'Tahun Masuk', 'Total Poin']
    data_profile_student = list(select_items('*', "mahasiswa", f"WHERE id = {student_id}")[0][0])
    create_profile_page(frame_student, data_profile_student, header_student_profile, 1, 0)


def filter_options_events_students(event, jenis):
    typed_text = entry_var_events_students.get()
    filtered_options = [option for option in options_events_students if typed_text.lower() in option[0].lower()]
    frame_student_listbox.delete(0, tk.END)
    for option in filtered_options:
        frame_student_listbox.insert(tk.END, option[0])

def filtering_events_students():
    name_filter = entry_var_events_students.get().lower() 
    data = get_data_from_mysql_events_students(name_filter)  
    display_data_events_students(data) 

def input_to_log_students():
    student_id = frame_login_entry_username.get()
    event_name = entry_var_events_students.get().strip().lower()  # Ambil nama event dari input
    query_event_details = 'SELECT id, status, point FROM events WHERE LOWER(name) = %s'
    cursor.execute(query_event_details, (event_name,))
    event_details = cursor.fetchone()

    if event_details:  # Jika event ditemukan di database
        event_id, event_status, event_point = event_details
        
        # Cek apakah event sudah diikuti oleh mahasiswa
        query_check_log = 'SELECT 1 FROM log_mahasiswa WHERE id_mahasiswa = %s AND id_event = %s'
        cursor.execute(query_check_log, (student_id, event_id))
        log_exists = cursor.fetchone()
        
        if log_exists:  # Jika sudah ada di log
            messagebox.showwarning("Peringatan", "Event ini sudah pernah diikuti oleh Anda.")
        elif event_status.lower() != "available":  # Jika status event tidak tersedia
            messagebox.showwarning("Peringatan", "Event tidak tersedia untuk diikuti.")
        else:  # Jika event tersedia dan belum diikuti, tambahkan ke log
            try:
                # Tambahkan ke log mahasiswa
                insert_values("log_mahasiswa", "id_mahasiswa, id_event", [(student_id, event_id)])
                query_update_points = '''
                    UPDATE mahasiswa 
                    SET points_earned = points_earned + %s
                    WHERE id = %s
                '''
                cursor.execute(query_update_points, (event_point, student_id))
                commit() 

                # Perbarui listbox dan treeview
                load_all_data_events_students()
                data_profile_student = list(select_items('*', "mahasiswa", f"WHERE id = {student_id}")[0][0])
                header_student_profile = ['Id', 'Password', 'Nama', 'Prodi', 'Email', 'Nomor Kontak', 'Tahun Masuk', 'Total Poin']
                create_profile_page(frame_student, data_profile_student, header_student_profile, 1, 0)

                
                messagebox.showinfo("Sukses", "Event berhasil dimasukkan ke log.")
            except Exception as e:
                messagebox.showerror("Error", f"Gagal menambahkan event ke log: {e}")
    else:
        messagebox.showerror("Error", "Event tidak ditemukan.")

def load_all_data_events_students():
    data = get_data_listbox_from_mysql_events_students("")  # Ambil semua data dari database
    
    # Filter untuk listbox (hanya event yang belum diikuti)
    listbox_data = [row for row in data if row[-1] == "Belum Diikuti"]
    # Refresh treeview
    display_data_events_students(data)  # Load data ke treeview
    
    # Refresh listbox
    frame_student_listbox.delete(0, tk.END)
    for row in listbox_data:
        frame_student_listbox.insert(tk.END, row[0])  # Masukkan nama event ke listbox

def get_data_from_mysql_events_students(name_filter):
    student_id = frame_login_entry_username.get()
    try:
        query = '''
                SELECT 
                    e.name, e.status, e.category, e.speaker, e.date, e.time, e.point, e.max_repetition,
                    CASE 
                        WHEN se.id_event IS NOT NULL THEN 'Sudah Diikuti'
                        ELSE 'Belum Diikuti'
                    END AS status_tamb
                FROM events AS e
                LEFT JOIN log_mahasiswa AS se 
                ON e.id = se.id_event AND se.id_mahasiswa = %s
                WHERE e.name LIKE %s
                ORDER BY 
                    status_tamb ASC,
                    e.status ASC,
                    e.id ASC;
                '''
        cursor.execute(query, (student_id, '%' + name_filter + '%'))
        rows = cursor.fetchall()
        return rows if rows else []
    except Exception as e:
        print(f"Error fetching filtered data: {e}")
        return []
    
def get_data_listbox_from_mysql_events_students(name_filter):
    student_id = frame_login_entry_username.get()
    try:
        query = '''
                SELECT 
                    e.name, e.status, e.category, e.speaker, e.date, e.time, e.point, e.max_repetition,
                    CASE 
                        WHEN se.id_event IS NOT NULL THEN 'Sudah Diikuti'
                        ELSE 'Belum Diikuti'
                    END AS status_tamb
                FROM events AS e
                LEFT JOIN log_mahasiswa AS se 
                ON e.id = se.id_event AND se.id_mahasiswa = %s
                WHERE e.name LIKE %s AND e.status = 'available'
                ORDER BY 
                    status_tamb ASC,
                    e.status ASC,
                    e.id ASC;
                '''
        cursor.execute(query, (student_id, '%' + name_filter + '%'))
        rows = cursor.fetchall()
        listbox_data = [row for row in rows if row[-1] == "Belum Diikuti"]
        return rows if rows else []
    except Exception as e:
        print(f"Error fetching filtered data: {e}")
        return []

def display_data_events_students(data):
    for i in frame_student_tree.get_children():
        frame_student_tree.delete(i)  # Menghapus data lama
    for row in data:
        frame_student_tree.insert("", "end", values=row)

def display_listbox_data_events_students(options_events_students):
    frame_student_listbox.delete(0, tk.END)
    for option in options_events_students:
        frame_student_listbox.insert(tk.END, option[0])

# Tombol dan input
frame_student_home_button = ttk.Button(frame_student, text='Log Out', width=0, command=lambda: show_frame('login'))
frame_student_home_button.grid(row=0, column=0, padx=10, ipady=5, pady=5, sticky='w')

frame_show_students_home_button = ttk.Button(frame_student, text='↻', width=0, command=load_all_data_events_students)
frame_show_students_home_button.grid(row=0, column=1, padx=10, ipady=5, pady=5, sticky='w')

entry_var_events_students = tk.StringVar()
options_events_students = get_data_listbox_from_mysql_events_students('')

frame_student_input = ttk.LabelFrame(frame_student, text='SEARCH')
frame_student_input.grid(row=2, column=0, sticky='n')

frame_student_name_entry = ttk.Entry(frame_student_input, textvariable=entry_var_events_students, width=20)
frame_student_name_entry.grid(row=0, column=0, padx=(5, 2), pady=5, sticky="n")
frame_student_name_entry.insert(0, "Nama Events")
frame_student_name_entry.config(foreground='grey')
frame_student_name_entry.bind("<FocusIn>", lambda event: on_click(event, frame_student_name_entry))
frame_student_name_entry.bind("<FocusOut>", lambda event: on_focusout(event, frame_student_name_entry, 'Nama Events'))

frame_student_listbox = tk.Listbox(frame_student_input, width=20, selectmode=tk.SINGLE)
frame_student_listbox.grid(row=0, column=1, padx=(2, 5), pady=5, sticky="ew") 

frame_student_name_entry.bind("<KeyRelease>", lambda event: filter_options_events_students(entry_var_events_students.get(), frame_student_listbox))
frame_student_listbox.bind("<<ListboxSelect>>", lambda event: on_select(event, entry_var_events_students))

frame_student_submit_button = ttk.Button(frame_student_input, text='SEARCH', command=filtering_events_students)
frame_student_submit_button.grid(row=1, column=0, padx=5, pady=5, sticky='ew')

frame_student_submit_button = ttk.Button(frame_student_input, text='INPUT', command=input_to_log_students)
frame_student_submit_button.grid(row=1, column=1, padx=5, pady=5, sticky='ew')

frame_student_Label = ttk.LabelFrame(frame_student, text='DATA EVENTS')
frame_student_Label.grid(row=2, column=1, ipadx=5, ipady=5)

columns = ('Nama', 'Status', 'Kategory', 'Speaker', 'Tanggal', 'Pukul', 'Poin', 'Max Repetition', 'Status Keikutsertaan')  
frame_student_tree = ttk.Treeview(frame_student_Label, columns=columns, show="headings")
frame_student_tree.grid(row=0, column=0)

for col in columns:
    frame_student_tree.heading(col, text=col)
    frame_student_tree.column(col, width=75)  

tree_scroll = ttk.Scrollbar(frame_student_Label, orient="vertical", command=frame_student_tree.yview)
tree_scroll.grid(row=0, column=1, sticky='ns') 
frame_student_tree.config(yscrollcommand=tree_scroll.set)

load_all_data_events_students()
     

""" Frame: Staff """
def staff_profile():
    staff_id = frame_login_entry_username.get()
    header_staffs_profile = ['Id', 'Password', 'Nama', 'Bidang', 'Email', 'Nomor Kontak', 'Tanggal Bergabung']
    data_profile_staff = list(select_items('*', "staff", f"WHERE id = {staff_id}")[0][0])
    create_profile_page(frame_staff, data_profile_staff, header_staffs_profile, 1, 0)

def filter_options_events_staffs(event, jenis):
    typed_text = entry_var_events_staffs.get()
    filtered_options = [option for option in options_events_staffs if typed_text.lower() in option[0].lower()]
    frame_staff_listbox.delete(0, tk.END)
    for option in filtered_options:
        frame_staff_listbox.insert(tk.END, option[0])

def filtering_events_staffs():
    name_filter = entry_var_events_staffs.get().lower() 
    data = get_data_from_mysql_events_staffs(name_filter)  
    display_data_events_staffs(data) 

def input_to_log_staffs():
    staff_id = frame_login_entry_username.get()
    event_name = entry_var_events_staffs.get().strip().lower()  # Ambil nama event dari input
    query_event_details = 'SELECT id, status, point FROM events WHERE LOWER(name) = %s'
    cursor.execute(query_event_details, (event_name,))
    event_details = cursor.fetchone()

    if event_details:  # Jika event ditemukan di database
        event_id, event_status, event_point = event_details
        
        # Cek apakah event sudah diikuti oleh staff
        query_check_log = 'SELECT 1 FROM log_staff WHERE id_staff = %s AND id_event = %s'
        cursor.execute(query_check_log, (staff_id, event_id))
        log_exists = cursor.fetchone()
        
        if log_exists:  # Jika sudah ada di log
            messagebox.showwarning("Peringatan", "Event ini sudah pernah diikuti oleh Anda.")
        elif event_status.lower() != "available":  # Jika status event tidak tersedia
            messagebox.showwarning("Peringatan", "Event tidak tersedia untuk diikuti.")
        else:  # Jika event tersedia dan belum diikuti, tambahkan ke log
            try:
                # Tambahkan ke log staff
                insert_values("log_staff", "id_staff, id_event", [(staff_id, event_id)])
                commit()
                # Perbarui listbox dan treeview
                load_all_data_events_staffs()
                data_profile_staff = list(select_items('*', "staff", f"WHERE id = {staff_id}")[0][0])
                header_staff_profile = ['Id', 'Password', 'Nama', 'Bidang', 'Email', 'Nomor Kontak', 'Tanggal Bergabung']
                create_profile_page(frame_staff, data_profile_staff, header_staff_profile, 1, 0)
                
                messagebox.showinfo("Sukses", "Event berhasil dimasukkan ke log.")
            except Exception as e:
                messagebox.showerror("Error", f"Gagal menambahkan event ke log: {e}")
    else:
        messagebox.showerror("Error", "Event tidak ditemukan.")

def load_all_data_events_staffs():
    data = get_data_listbox_from_mysql_events_staffs("")  # Ambil semua data dari database
    
    # Filter untuk listbox (hanya event yang belum diikuti)
    listbox_data = [row for row in data if row[-1] == "Belum Diikuti"]
    
    # Refresh treeview
    display_data_events_staffs(data)  # Load data ke treeview
    
    # Refresh listbox
    frame_staff_listbox.delete(0, tk.END)
    for row in listbox_data:
        frame_staff_listbox.insert(tk.END, row[0])  # Masukkan nama event ke listbox

def get_data_from_mysql_events_staffs(name_filter):
    staff_id = frame_login_entry_username.get()
    try:
        query = '''
                SELECT 
                    e.name, e.status, e.category, e.speaker, e.date, e.time, 
                    CASE 
                        WHEN se.id_event IS NOT NULL THEN 'Sudah Diikuti'
                        ELSE 'Belum Diikuti'
                    END AS status_tamb
                FROM events AS e
                LEFT JOIN log_staff AS se 
                ON e.id = se.id_event AND se.id_staff = %s
                WHERE e.name LIKE %s
                ORDER BY 
                    status_tamb ASC,
                    e.status ASC,
                    e.id ASC;
                '''
        cursor.execute(query, (staff_id, '%' + name_filter + '%'))
        rows = cursor.fetchall()
        return rows if rows else []
    except Exception as e:
        print(f"Error fetching filtered data: {e}")
        return []
    
def get_data_listbox_from_mysql_events_staffs(name_filter):
    staff_id = frame_login_entry_username.get()
    try:
        query = '''
                SELECT 
                    e.name, e.status, e.category, e.speaker, e.date, e.time,
                    CASE 
                        WHEN se.id_event IS NOT NULL THEN 'Sudah Diikuti'
                        ELSE 'Belum Diikuti'
                    END AS status_tamb
                FROM events AS e
                LEFT JOIN log_staff AS se 
                ON e.id = se.id_event AND se.id_staff = %s
                WHERE e.name LIKE %s AND e.status = 'available'
                ORDER BY 
                    status_tamb ASC,
                    e.status ASC,
                    e.id ASC;
                '''
        cursor.execute(query, (staff_id, '%' + name_filter + '%'))
        rows = cursor.fetchall()
        listbox_data = [row for row in rows if row[-1] == "Belum Diikuti"]
        return rows if rows else []
    except Exception as e:
        print(f"Error fetching filtered data: {e}")
        return []

def display_data_events_staffs(data):
    for i in frame_staff_tree.get_children():
        frame_staff_tree.delete(i)  # Menghapus data lama
    for row in data:
        frame_staff_tree.insert("", "end", values=row)

def display_listbox_data_events_staffs(options_events_staffs):
    frame_staff_listbox.delete(0, tk.END)
    for option in options_events_staffs:
        frame_staff_listbox.insert(tk.END, option[0])

# Tombol dan input
frame_staff_home_button = ttk.Button(frame_staff, text='Log Out', width=0, command=lambda: show_frame('login'))
frame_staff_home_button.grid(row=0, column=0, padx=10, ipady=5, pady=5, sticky='w')

frame_show_staffs_home_button = ttk.Button(frame_staff, text='↻', width=0, command=load_all_data_events_staffs)
frame_show_staffs_home_button.grid(row=0, column=1, padx=10, ipady=5, pady=5, sticky='w')

entry_var_events_staffs = tk.StringVar()
options_events_staffs = get_data_listbox_from_mysql_events_staffs('')

frame_staff_input = ttk.LabelFrame(frame_staff, text='SEARCH')
frame_staff_input.grid(row=2, column=0, sticky='n')

frame_staff_name_entry = ttk.Entry(frame_staff_input, textvariable=entry_var_events_staffs, width=20)
frame_staff_name_entry.grid(row=0, column=0, padx=(5, 2), pady=5, sticky="n")
frame_staff_name_entry.insert(0, "Nama Events")
frame_staff_name_entry.config(foreground='grey')
frame_staff_name_entry.bind("<FocusIn>", lambda event: on_click(event, frame_staff_name_entry))
frame_staff_name_entry.bind("<FocusOut>", lambda event: on_focusout(event, frame_staff_name_entry, 'Nama Events'))

frame_staff_listbox = tk.Listbox(frame_staff_input, width=20, selectmode=tk.SINGLE)
frame_staff_listbox.grid(row=0, column=1, padx=(2, 5), pady=5, sticky="ew") 

frame_staff_name_entry.bind("<KeyRelease>", lambda event: filter_options_events_staffs(entry_var_events_staffs.get(), frame_staff_listbox))
frame_staff_listbox.bind("<<ListboxSelect>>", lambda event: on_select(event, entry_var_events_staffs))

frame_staff_submit_button = ttk.Button(frame_staff_input, text='SEARCH', command=filtering_events_staffs)
frame_staff_submit_button.grid(row=1, column=0, padx=5, pady=5, sticky='ew')

frame_staff_submit_button = ttk.Button(frame_staff_input, text='INPUT', command=input_to_log_staffs)
frame_staff_submit_button.grid(row=1, column=1, padx=5, pady=5, sticky='ew')

frame_staff_Label = ttk.LabelFrame(frame_staff, text='DATA EVENTS')
frame_staff_Label.grid(row=2, column=1, ipadx=5, ipady=5)

columns = ('Nama', 'Status', 'Kategory', 'Speaker', 'Tanggal', 'Pukul', 'Status Keikutsertaan')  
frame_staff_tree = ttk.Treeview(frame_staff_Label, columns=columns, show="headings")
frame_staff_tree.grid(row=0, column=0)

for col in columns:
    frame_staff_tree.heading(col, text=col)
    frame_staff_tree.column(col, width=75)  

tree_scroll = ttk.Scrollbar(frame_staff_Label, orient="vertical", command=frame_staff_tree.yview)
tree_scroll.grid(row=0, column=1, sticky='ns') 
frame_staff_tree.config(yscrollcommand=tree_scroll.set)

load_all_data_events_staffs()

""" Frame Admin """
frame_admin_button_width = 35
# menu berkaitan dengan event
frame_admin_label_event = ttk.LabelFrame(frame_admin, text='KEGIATAN')
frame_admin_label_event.grid(row=0, column=0, padx=20, pady=20)
frame_admin_button_show_event = ttk.Button(frame_admin_label_event, text='Menampilkan Semua Kegiatan', width=frame_admin_button_width, command=lambda: show_frame('show_events'))
frame_admin_button_show_event.grid(row=0, column=0, padx=5, pady=5)
frame_admin_button_new_event = ttk.Button(frame_admin_label_event, text='Menambahkan Kegiatan Baru', width=frame_admin_button_width, command=lambda: show_frame('new_events'))
frame_admin_button_new_event.grid(row=1, column=0, padx=5, pady=5)

# menu berkaitan dengan mahasiswa
frame_admin_label_mahasiswa = ttk.LabelFrame(frame_admin, text='MAHASISWA')
frame_admin_label_mahasiswa.grid(row=1, column=0, padx=20, pady=20)
frame_admin_button_show_mahasiswa = ttk.Button(frame_admin_label_mahasiswa, text='Menampilkan Data Mahasiswa', width=frame_admin_button_width, command=lambda: show_frame('show_students'))
frame_admin_button_show_mahasiswa.grid(row=0, column=0, padx=5, pady=5)
frame_admin_button_new_mahasiswa = ttk.Button(frame_admin_label_mahasiswa, text='Menambahkan Data Mahasiswa', width=frame_admin_button_width, command=lambda: show_frame('new_students'))
frame_admin_button_new_mahasiswa.grid(row=1, column=0, padx=5, pady=5)

# menu berkaitan dengan staff
frame_admin_label_staff = ttk.LabelFrame(frame_admin, text='STAFF')
frame_admin_label_staff.grid(row=2, column=0, padx=20, pady=20)
frame_admin_button_show_staff = ttk.Button(frame_admin_label_staff, text='Menampilkan Data Staff', width=frame_admin_button_width, command=lambda: show_frame('show_staffs'))
frame_admin_button_show_staff.grid(row=0, column=0, padx=5, pady=5)
frame_admin_button_new_staff = ttk.Button(frame_admin_label_staff, text='Menambahkan Data Staff', width=frame_admin_button_width, command=lambda: show_frame('new_staff'))
frame_admin_button_new_staff.grid(row=1, column=0, padx=5, pady=5)

# menu berkaitan dengan rekap
frame_admin_label_check_attendance = ttk.LabelFrame(frame_admin, text='REKAP')
frame_admin_label_check_attendance.grid(row=3, column=0, padx=20, pady=20)
frame_admin_button_check_attendance = ttk.Button(frame_admin_label_check_attendance, text='Check Kehadiran & Edit', width=frame_admin_button_width, command=lambda: show_frame('check_attendance'))
frame_admin_button_check_attendance.grid(row=0, column=0, padx=5, pady=5)

frame_admin_logout = ttk.Button(frame_admin, text='Log Out', command=lambda: show_frame('login'))
frame_admin_logout.grid(row=4, column=0, columnspan=2, pady=5)
frame_admin.grid_columnconfigure(0, weight=1)


""" Frame Admin: Show Events + Ubah Status """
def on_select(event, entry):
    widget = event.widget
    selected_index = widget.curselection()
    if selected_index:
        selected_option = widget.get(selected_index[0])
        entry.set(selected_option)

def on_click(event, entry):
    entry.delete(0, tk.END)

def on_focusout(event, entry, text):
    if not entry.get():
        entry.insert(0, text)
        entry.config(foreground='grey')
        entry.focus_set()

def filter_options_events(event):
    typed_text = entry_var_events.get()
    filtered_options = [option for option in options_events if typed_text.lower() in option.lower()]
    frame_show_events_listbox.delete(0, tk.END)
    for option in filtered_options:
        frame_show_events_listbox.insert(tk.END, option)

def fetch_all_data_events():
    return select_items("name", "events")[0]

def filtering_events():
    name_filter = entry_var_events.get().lower() 
    data = get_data_from_mysql_events(name_filter)
    if data == None: return  
    display_data_events(data) 

def get_data_from_mysql_events(name_filter):
    if name_filter:  # Jika ada filter
        rows = select_items("*", "events", f"WHERE LOWER(name) LIKE '%{name_filter}%'")
    else:  # Jika tidak ada filter, ambil semua data
        rows = select_items("*", "events")
    if rows == None: return
    return rows[0]

def display_data_events(data):
    for i in frame_show_events_tree.get_children():
        frame_show_events_tree.delete(i)  # Menghapus data lama
    for row in data:
        frame_show_events_tree.insert("", "end", values=row)

def load_all_data_events():
    data = get_data_from_mysql_events("")  
    display_data_events(data)

def list_box_events():
    global options_events
    frame_show_events_listbox.delete(0, tk.END)
    options_events = fetch_all_data_events()
    for option in options_events:
        frame_show_events_listbox.insert(tk.END, option)

def change_status_events():
    global frame_show_events_confirm_button
    name_events = entry_var_events.get()
    if name_events not in select_items("name", "events")[0]:
        frame_show_events_label_result.config(text='Event tidak ditemukan', foreground="red", justify="center")
        return
    
    def change_status_events_confirmed():
        frame_show_events_label_result.config(text='Status berhasil diubah!', foreground="blue", justify="center")
        frame_show_events_confirm_button.grid_forget()
        frame_show_events_submit_button.grid(row=2, column=0, padx=5, pady=5)
        frame_show_events_change_button.grid(row=2, column=1, padx=5, pady=5)
        update_table('events', f'status = "{"not available" if current_status == "available" else "available"}"', f"name = '{name_events}'")
        commit()
        load_all_data_events()

    current_status = select_items("status", "events", f"where name = '{name_events}'")[0][0]
    frame_show_events_label_result.config(text=f'Yakin ingin mengubah status\n{name_events}\nmenjadi {"not available" if current_status == "available" else "available"}?', foreground="blue", justify="center")
    frame_show_events_confirm_button = ttk.Button(frame_show_events_input, text='Confirm', command=change_status_events_confirmed)
    frame_show_events_confirm_button.grid(row=2, column=0, columnspan=2, pady=5)
    frame_show_events_submit_button.grid_forget()
    frame_show_events_change_button.grid_forget()

def back_to_admin_from_events():
    show_frame('admin')
    frame_show_events_label_result.config(text='', foreground="blue", justify="center")
    frame_show_events_confirm_button.grid_forget()
    frame_show_events_submit_button.grid(row=2, column=0, padx=5, pady=5)
    frame_show_events_change_button.grid(row=2, column=1, padx=5, pady=5)

frame_show_events_home_button = ttk.Button(frame_show_events, text='🏠︎', width=0, command=back_to_admin_from_events)
frame_show_events_home_button.grid(row=0, column=0, padx=10, ipady=5, pady=5, sticky='w')
frame_show_events_reset_button = ttk.Button(frame_show_events, text='↻', width=0, command=load_all_data_events)
frame_show_events_reset_button.grid(row=0, column=1, padx=10, ipady=5, pady=5, sticky='w')

entry_var_events = tk.StringVar()
frame_show_events_input = ttk.LabelFrame(frame_show_events, text='SEARCH')
frame_show_events_input.grid(row=1, column=0, sticky='n')
frame_show_events_name_entry = ttk.Entry(frame_show_events_input, textvariable=entry_var_events, width=20)
frame_show_events_name_entry.grid(row=0, column=0, padx=(5, 2), pady=5, sticky="n")
frame_show_events_name_entry.insert(0, "Nama Events")
frame_show_events_name_entry.config(foreground='grey')
frame_show_events_name_entry.bind("<FocusIn>", lambda event:on_click(event, frame_show_events_name_entry))
frame_show_events_name_entry.bind("<FocusOut>", lambda event:on_focusout(event, frame_show_events_name_entry, 'Nama Events'))

frame_show_events_listbox = tk.Listbox(frame_show_events_input, width=20, selectmode=tk.SINGLE)
frame_show_events_listbox.grid(row=0, column=1, padx=(2, 5), pady=5, sticky="ew") 
list_box_events()
frame_show_events_name_entry.bind("<KeyRelease>", filter_options_events)
frame_show_events_listbox.bind("<<ListboxSelect>>", lambda event: on_select(event, entry_var_events))

frame_show_events_label_result = ttk.Label(frame_show_events_input, text="", foreground="red", justify="center")
frame_show_events_label_result.grid(row=1, column=0, columnspan=2, pady=5)
frame_show_events_submit_button = ttk.Button(frame_show_events_input, text='SEARCH', command=filtering_events)
frame_show_events_submit_button.grid(row=2, column=0, padx=5, pady=5)
frame_show_events_change_button = ttk.Button(frame_show_events_input, text='Change Status', command=change_status_events)
frame_show_events_change_button.grid(row=2, column=1, padx=5, pady=5)
frame_show_events_confirm_button = ttk.Button(frame_show_events_input)

frame_show_events_Label = ttk.LabelFrame(frame_show_events, text='DATA EVENTS')
frame_show_events_Label.grid(row=1, column=1, ipadx=5, ipady=5, sticky='n')
columns = ('Id', 'Nama', 'Status', 'Kategori', 'Pembicara', 'Tanggal', 'Pukul', 'Poin', 'Maksimum Pengulangan (bagi mahasiswa)')  
frame_show_events_tree = ttk.Treeview(frame_show_events_Label, columns=columns, show="headings")
for col in columns:
    frame_show_events_tree.heading(col, text=col)
    frame_show_events_tree.column(col, width=75)  
frame_show_events_tree.grid(row=0, column=0)
tree_scroll = ttk.Scrollbar(frame_show_events_Label, orient="vertical", command=frame_show_events_tree.yview)
tree_scroll.grid(row=0, column=1, sticky='ns') 
frame_show_events_tree.config(yscrollcommand=tree_scroll.set)
load_all_data_events()


""" Frame Admin: Show Mahasiswa """
def filter_options_students(student):
    typed_text = entry_var_students.get()
    filtered_options = [option for option in options_students if typed_text.lower() in option.lower()]
    frame_show_students_listbox.delete(0, tk.END)
    for option in filtered_options:
        frame_show_students_listbox.insert(tk.END, option)

def fetch_all_data_students():
    return select_items("name", "mahasiswa")[0]

def filtering_students():
    name_filter = entry_var_students.get().lower() 
    data = get_data_from_mysql_students(name_filter)  
    if data == None: return
    display_data_students(data) 

def get_data_from_mysql_students(name_filter):
    if name_filter:  # Jika ada filter
        rows = select_items("*", "mahasiswa", f"WHERE LOWER(name) LIKE '%{name_filter}%'")
    else:  # Jika tidak ada filter, ambil semua data
        rows = select_items("*", "mahasiswa")
    if rows == None: return
    return rows[0]

def display_data_students(data):
    for i in frame_show_students_tree.get_children():
        frame_show_students_tree.delete(i)  # Menghapus data lama
    for row in data:
        frame_show_students_tree.insert("", "end", values=row)

def load_all_data_students():
    data = get_data_from_mysql_students("")  
    display_data_students(data)

def list_box_students():
    global options_students
    frame_show_students_listbox.delete(0, tk.END)
    options_students = fetch_all_data_students()
    for option in options_students:
        frame_show_students_listbox.insert(tk.END, option)

def back_to_admin_from_students():
    show_frame('admin')
    frame_show_students_label_result.config(text='', foreground="blue", justify="center")
    frame_show_students_confirm_button.grid_forget()
    frame_show_students_search_button.grid(row=2, column=0, padx=5, pady=5)
    frame_show_students_delete_button.grid(row=2, column=1, padx=5, pady=5)

def delete_students():
    global frame_show_students_confirm_button
    name_students = entry_var_students.get()
    if name_students not in select_items("name", "mahasiswa")[0]:
        frame_show_students_label_result.config(text='Mahasiswa tidak ditemukan', foreground="red", justify="center")
        return

    def change_status_students_confirmed():
        frame_show_students_label_result.config(text='Mahasiswa berhasil dihapus!', foreground="blue", justify="center")
        frame_show_students_confirm_button.grid_forget()
        frame_show_students_search_button.grid(row=2, column=0, padx=5, pady=5)
        frame_show_students_delete_button.grid(row=2, column=1, padx=5, pady=5)
        id_students = select_items('id', 'mahasiswa', f"where name = '{name_students}'")[0][0]
        delete_items("log_mahasiswa", f"id_mahasiswa = '{id_students}'")
        delete_items("mahasiswa", f"name = '{name_students}'")
        commit()
        list_box_students()
        load_all_data_students()

    frame_show_students_label_result.config(text=f'Yakin ingin menghapus mahasiswa\n{name_students}?', foreground="blue", justify="center")
    frame_show_students_confirm_button = ttk.Button(frame_show_students_input, text='Confirm', command=change_status_students_confirmed)
    frame_show_students_confirm_button.grid(row=2, column=0, columnspan=2, pady=5)
    frame_show_students_search_button.grid_forget()
    frame_show_students_delete_button.grid_forget()
    
frame_show_students_home_button = ttk.Button(frame_show_students, text='🏠︎', width=0, command=back_to_admin_from_students)
frame_show_students_home_button.grid(row=0, column=0, padx=10, ipady=5, pady=5, sticky='w')
frame_show_students_reset_button = ttk.Button(frame_show_students, text='↻', width=0, command=load_all_data_students)
frame_show_students_reset_button.grid(row=0, column=1, padx=10, ipady=5, pady=5, sticky='w')

entry_var_students = tk.StringVar()
frame_show_students_input = ttk.LabelFrame(frame_show_students, text='SEARCH')
frame_show_students_input.grid(row=1, column=0, sticky='n')
frame_show_students_name_entry = ttk.Entry(frame_show_students_input, textvariable=entry_var_students, width=20)
frame_show_students_name_entry.grid(row=0, column=0, padx=(5, 2), pady=5, sticky="n")
frame_show_students_name_entry.insert(0, "Nama Mahasiswa")
frame_show_students_name_entry.config(foreground='grey')
frame_show_students_name_entry.bind("<FocusIn>", lambda event:on_click(event, frame_show_students_name_entry))
frame_show_students_name_entry.bind("<FocusOut>", lambda event:on_focusout(event, frame_show_students_name_entry, 'Nama Mahasiswa'))

frame_show_students_listbox = tk.Listbox(frame_show_students_input, width=20, selectmode=tk.SINGLE)
frame_show_students_listbox.grid(row=0, column=1, padx=(2, 5), pady=5, sticky="ew") 
list_box_students()
frame_show_students_name_entry.bind("<KeyRelease>", filter_options_students)
frame_show_students_listbox.bind("<<ListboxSelect>>", lambda event: on_select(event, entry_var_students))

frame_show_students_label_result = ttk.Label(frame_show_students_input, text="", foreground="red", justify="center")
frame_show_students_label_result.grid(row=1, column=0, columnspan=2, pady=5)
frame_show_students_search_button = ttk.Button(frame_show_students_input, text='SEARCH', command=filtering_students)
frame_show_students_search_button.grid(row=2, column=0, padx=5, pady=5)
frame_show_students_delete_button = ttk.Button(frame_show_students_input, text='DELETE', command=delete_students)
frame_show_students_delete_button.grid(row=2, column=1, padx=5, pady=5)
frame_show_students_confirm_button = ttk.Button(frame_show_students_input)

frame_show_students_Label = ttk.LabelFrame(frame_show_students, text='DATA MAHASISWA')
frame_show_students_Label.grid(row=1, column=1, ipadx=5, ipady=5, sticky='n')
columns = ('Id', 'Password', 'Nama', 'Prodi', 'Email', 'Nomor Telepon', 'Angkatan', 'Total Poin')  
frame_show_students_tree = ttk.Treeview(frame_show_students_Label, columns=columns, show="headings")
for col in columns:
    frame_show_students_tree.heading(col, text=col)
    frame_show_students_tree.column(col, width=75)  
frame_show_students_tree.grid(row=0, column=0)
tree_scroll = ttk.Scrollbar(frame_show_students_Label, orient="vertical", command=frame_show_students_tree.yview)
tree_scroll.grid(row=0, column=1, sticky='ns') 
frame_show_students_tree.config(yscrollcommand=tree_scroll.set)
load_all_data_students()


""" Frame Admin: Show Staff """
def filter_options_staffs(student):
    typed_text = entry_var_staffs.get()
    filtered_options = [option for option in options_staffs if typed_text.lower() in option.lower()]
    frame_show_staffs_listbox.delete(0, tk.END)
    for option in filtered_options:
        frame_show_staffs_listbox.insert(tk.END, option)

def fetch_all_data_staffs():
    return select_items("name", "staff")[0]

def filtering_staffs():
    name_filter = entry_var_staffs.get().lower() 
    data = get_data_from_mysql_staffs(name_filter)  
    if data == None: return
    display_data_staffs(data) 

def get_data_from_mysql_staffs(name_filter):
    if name_filter:  # Jika ada filter
        rows = select_items("*", "staff", f"WHERE LOWER(name) LIKE '%{name_filter}%'")
    else:  # Jika tidak ada filter, ambil semua data
        rows = select_items("*", "staff")
    if rows == None: return
    return rows[0]

def display_data_staffs(data):
    for i in frame_show_staffs_tree.get_children():
        frame_show_staffs_tree.delete(i)  # Menghapus data lama
    for row in data:
        frame_show_staffs_tree.insert("", "end", values=row)

def load_all_data_staffs():
    data = get_data_from_mysql_staffs("")  
    display_data_staffs(data)

def list_box_staffs():
    global options_staffs
    frame_show_staffs_listbox.delete(0, tk.END)
    options_staffs = fetch_all_data_staffs()
    for option in options_staffs:
        frame_show_staffs_listbox.insert(tk.END, option)

def back_to_admin_from_staffs():
    show_frame('admin')
    frame_show_staffs_label_result.config(text='', foreground="blue", justify="center")
    frame_show_staffs_confirm_button.grid_forget()
    frame_show_staffs_search_button.grid(row=2, column=0, padx=5, pady=5)
    frame_show_staffs_delete_button.grid(row=2, column=1, padx=5, pady=5)

def delete_staffs():
    global frame_show_staffs_confirm_button
    name_staff = entry_var_staffs.get()
    if name_staff not in select_items("name", "staff")[0]:
        frame_show_staffs_label_result.config(text='Staff tidak ditemukan', foreground="red", justify="center")
        return

    def change_status_staffs_confirmed():
        frame_show_staffs_label_result.config(text='Staff berhasil dihapus!', foreground="blue", justify="center")
        frame_show_staffs_confirm_button.grid_forget()
        frame_show_staffs_search_button.grid(row=2, column=0, padx=5, pady=5)
        frame_show_staffs_delete_button.grid(row=2, column=1, padx=5, pady=5)
        id_staff = select_items('id', 'staff', f"where name = '{name_staff}'")[0][0]
        delete_items("log_staff", f"id_staff = '{id_staff}'")
        delete_items("staff", f"name = '{name_staff}'")
        commit()
        list_box_staffs()
        load_all_data_staffs()

    frame_show_staffs_label_result.config(text=f'Yakin ingin menghapus staff\n{name_staff}?', foreground="blue", justify="center")
    frame_show_staffs_confirm_button = ttk.Button(frame_show_staffs_input, text='Confirm', command=change_status_staffs_confirmed)
    frame_show_staffs_confirm_button.grid(row=2, column=0, columnspan=2, pady=5)
    frame_show_staffs_search_button.grid_forget()
    frame_show_staffs_delete_button.grid_forget()


frame_show_staffs_home_button = ttk.Button(frame_show_staffs, text='🏠︎', width=0, command=back_to_admin_from_staffs)
frame_show_staffs_home_button.grid(row=0, column=0, padx=10, ipady=5, pady=5, sticky='w')
frame_show_staffs_reset_button = ttk.Button(frame_show_staffs, text='↻', width=0, command=load_all_data_staffs)
frame_show_staffs_reset_button.grid(row=0, column=1, padx=10, ipady=5, pady=5, sticky='w')

entry_var_staffs = tk.StringVar()
frame_show_staffs_input = ttk.LabelFrame(frame_show_staffs, text='SEARCH')
frame_show_staffs_input.grid(row=1, column=0, sticky='n')
frame_show_staffs_name_entry = ttk.Entry(frame_show_staffs_input, textvariable=entry_var_staffs, width=20)
frame_show_staffs_name_entry.grid(row=0, column=0, padx=(5, 2), pady=5, sticky="n")
frame_show_staffs_name_entry.insert(0, "Nama Staff")
frame_show_staffs_name_entry.config(foreground='grey')
frame_show_staffs_name_entry.bind("<FocusIn>", lambda event:on_click(event, frame_show_staffs_name_entry))
frame_show_staffs_name_entry.bind("<FocusOut>", lambda event:on_focusout(event, frame_show_staffs_name_entry, 'Nama Staff'))

frame_show_staffs_listbox = tk.Listbox(frame_show_staffs_input, width=20, selectmode=tk.SINGLE)
frame_show_staffs_listbox.grid(row=0, column=1, padx=(2, 5), pady=5, sticky="ew") 
list_box_staffs()
frame_show_staffs_name_entry.bind("<KeyRelease>", filter_options_staffs)
frame_show_staffs_listbox.bind("<<ListboxSelect>>", lambda event: on_select(event, entry_var_staffs))

frame_show_staffs_label_result = ttk.Label(frame_show_staffs_input, text="", foreground="red", justify="center")
frame_show_staffs_label_result.grid(row=1, column=0, columnspan=2, pady=5)
frame_show_staffs_search_button = ttk.Button(frame_show_staffs_input, text='SEARCH', command=filtering_staffs)
frame_show_staffs_search_button.grid(row=2, column=0, padx=5, pady=5)
frame_show_staffs_delete_button = ttk.Button(frame_show_staffs_input, text='DELETE', command=delete_staffs)
frame_show_staffs_delete_button.grid(row=2, column=1, padx=5, pady=5)
frame_show_staffs_confirm_button = ttk.Button(frame_show_staffs_input)

frame_show_staffs_Label = ttk.LabelFrame(frame_show_staffs, text='DATA STAFF')
frame_show_staffs_Label.grid(row=1, column=1, ipadx=5, ipady=5, sticky='n')
columns = ('Id', 'Password', 'Nama', 'Jabatan', 'Email', 'Nomor Telepon', 'Tanggal Masuk')  
frame_show_staffs_tree = ttk.Treeview(frame_show_staffs_Label, columns=columns, show="headings")
for col in columns:
    frame_show_staffs_tree.heading(col, text=col)
    frame_show_staffs_tree.column(col, width=75)  
frame_show_staffs_tree.grid(row=0, column=0)
tree_scroll = ttk.Scrollbar(frame_show_staffs_Label, orient="vertical", command=frame_show_staffs_tree.yview)
tree_scroll.grid(row=0, column=1, sticky='ns') 
frame_show_staffs_tree.config(yscrollcommand=tree_scroll.set)
load_all_data_staffs()


""" Frame New Events """
def input_empty_validation(text, type):
    try:
        if len(text) == 0: raise ValueError
    except ValueError:
        frame_new_events_label_result.config(text=f'System: Input kosong.\nSilakan memasukkan {type}!', foreground="red", justify="center")
        frame_new_students_label_result.config(text=f'System: Input kosong.\nSilakan memasukkan {type}!', foreground="red", justify="center")
        frame_new_staffs_label_result.config(text=f'System: Input kosong.\nSilakan memasukkan {type}!', foreground="red", justify="center")
    else: return text

def input_unique_validation(text, input_category, invalid_type):
    if input_category == "mahasiswa" or input_category == "staff":
        input_id = text.strip()
        if input_id in select_items("id", "mahasiswa")[0] or input_id in select_items("id", "staff")[0]:
            frame_new_students_label_result.config(text=f'System: ID tidak valid karena sudah dipakai.\nSilakan memasukkan ID yang unique!', foreground="red", justify="center")
            frame_new_staffs_label_result.config(text=f'System: ID tidak valid karena sudah dipakai.\nSilakan memasukkan ID yang unique!', foreground="red", justify="center")
        else: return input_id
    else:
        input_id = text.strip().lower()
        if invalid_type == "ID" and input_id in list(map(lambda x: x.lower(), select_items("id", "events")[0])):
            frame_new_events_label_result.config(text=f'System: ID tidak valid karena sudah dipakai.\nSilakan memasukkan ID yang unique!', foreground="red", justify="center")
        elif invalid_type == "Name" and input_id in list(map(lambda x: x.lower(), select_items("name", "events")[0])):
            frame_new_events_label_result.config(text=f'System: Nama tidak valid karena sudah dipakai.\nSilakan memasukkan nama lain yang unique!', foreground="red", justify="center")
        else: return text

def input_date_validation(text):
    try:
        text = text.split('-')
        if len(text) > 3: raise IndexError
        for i in range(3):
            text[i] = int(text[i])
    except ValueError:
        frame_new_events_label_result.config(text="System: Input tidak valid.\nSilakan masukkan tanggal yang benar.", foreground="red", justify="center")
        frame_new_staffs_label_result.config(text="System: Input tidak valid.\nSilakan masukkan tanggal yang benar.", foreground="red", justify="center")
    except IndexError:
        frame_new_events_label_result.config(text="System: Input tidak valid.\nSilakan masukkan tanggal yang benar.", foreground="red", justify="center")
        frame_new_staffs_label_result.config(text="System: Input tidak valid.\nSilakan masukkan tanggal yang benar.", foreground="red", justify="center")
    else:
        if not 1 <= text[0] <= 31 or not 1 <= text[1] <= 12 or not 1900 <= text[2] <= 2100:
            frame_new_events_label_result.config(text="System: Input tidak valid.\nSilakan masukkan tanggal yang benar.", foreground="red", justify="center")
            frame_new_staffs_label_result.config(text="System: Input tidak valid.\nSilakan masukkan tanggal yang benar.", foreground="red", justify="center")
            return
        text[0] = '0' + str(text[0]) if len(str(text[0])) == 1 else str(text[0])
        text[1] = '0' + str(text[1]) if len(str(text[1])) == 1 else str(text[1])
        return '-'.join(map(str, text))
    
def input_time_validation(text):
    try:
        text = text.split(':')
        if len(text) > 2: raise IndexError
        for i in range(2):
            text[i] = int(text[i])
    except ValueError:
        frame_new_events_label_result.config(text="System: Input tidak valid.\nSilakan masukkan jam yang benar.", foreground="red", justify="center")
    except IndexError:
        frame_new_events_label_result.config(text="System: Input tidak valid.\nSilakan masukkan jam yang benar.", foreground="red", justify="center")
    else:
        if not 0 <= text[0] <= 23 or not 0 <= text[1] <= 59:
            frame_new_events_label_result.config(text="System: Input tidak valid.\nSilakan masukkan jam yang benar.", foreground="red", justify="center")
            return
        text[0] = '0' + str(text[0]) if len(str(text[0])) == 1 else str(text[0])
        text[1] = '0' + str(text[1]) if len(str(text[1])) == 1 else str(text[1])
        return ':'.join(map(str, text))
    
def input_float_validation(text):
    try:
        user_input = float(text)  
        if user_input > 99.99 or user_input < 0: raise ValueError
    except ValueError: frame_new_events_label_result.config(text="System: Input tidak valid.\nSilakan masukkan angka desimal yang benar.", foreground="red", justify="center")
    else: return round(user_input, 2)

def refresh_combobox_rekap():
    global event_names, event_ids, selected_event_id
    cursor.execute("SELECT id, name FROM events")
    events = cursor.fetchall()

    # Membuat combobox untuk memilih event
    event_names = [event[1] for event in events]
    event_ids = [event[0] for event in events]
    selected_event_combobox = ttk.Combobox(frame_check_attendance, values=event_names, textvariable=selected_event_id)
    selected_event_combobox.grid(row=0, column=2, padx=10)
    selected_event_combobox.set("Select an event")
    # Mengatur combobox callback untuk update pie chart
    def on_event_select(event):
        selected_event_name = selected_event_combobox.get()
        if selected_event_name != "Select an event":
            update_pie_charts(selected_event_name)
    
    # Set nilai default Combobox ke event pertama 
    if event_names:
        selected_event_combobox.set(event_names[0])  
        update_pie_charts(event_names[0]) 
    
    selected_event_combobox.bind("<<ComboboxSelected>>", on_event_select)
    
def input_int_validation(text):
    try:
        user_input = int(text)
        if user_input <= 0: raise ValueError
    except ValueError: frame_new_events_label_result.config(text="System: Input tidak valid.\nSilakan masukkan angka bulat yang benar.", foreground="red", justify="center")
    else: return user_input
    
def submit_new_events():
    if not (event_id := input_empty_validation(frame_new_events_entry_id.get(), 'ID')) or not (event_id := input_unique_validation(frame_new_events_entry_id.get(), 'events', "ID")): return 
    if not (event_name := input_empty_validation(frame_new_events_entry_name.get(), 'nama')) or not (event_name := input_unique_validation(frame_new_events_entry_name.get(), 'events', "Name")): return 
    if not (event_category := input_empty_validation(frame_new_events_entry_category.get(), 'kategori')): return 
    event_speaker = frame_new_events_entry_speaker.get()
    if not (event_date := input_date_validation(frame_new_events_entry_date.get())): return 
    if not (event_time := input_time_validation(frame_new_events_entry_time.get())): return
    if not (event_point := input_float_validation(frame_new_events_entry_point.get())): return
    if not (event_repetition := input_int_validation(frame_new_events_entry_repetition.get())): return
    frame_new_events_label_result.config(text="System: Kegiatan telah berhasil ditambahkan!", foreground="green", justify="center")
    insert_values("events", "id,name,status,category,speaker,date,time,point,max_repetition",
                [(event_id.upper(), event_name, "available", event_category, event_speaker, event_date, event_time, event_point, event_repetition)])
    commit()
    refresh_combobox_rekap()
    list_box_events()
    load_all_data_events()
    delete_entry_new_events()

def back_to_admin():
    show_frame('admin')
    frame_new_events_label_result.config(text="", foreground="green", justify="center")
    frame_new_students_label_result.config(text="", foreground="green", justify="center")
    frame_new_staffs_label_result.config(text="", foreground="green", justify="center")
    frame_show_students_name_entry.config(text="Nama Mahasiswa", foreground='grey')
    delete_entry_new_students()
    delete_entry_new_events()
    delete_entry_new_staffs()
 
def delete_entry_new_events():
    for i in ("id","name","category","speaker","date","time","point","repetition"):
        exec(f"frame_new_events_entry_{i}.delete(0, tk.END)")

frame_new_events_back = ttk.Button(frame_new_events, text='Back', command=back_to_admin)
frame_new_events_back.grid(row=0, column=0, padx=5, pady=5)
frame_new_events_label = ttk.LabelFrame(frame_new_events, text='New Events')
frame_new_events_label.grid(row=1, column=0, columnspan=2, pady=5)

for no, i in enumerate(("id","name","category","speaker","date","time","point","repetition")):
    dictLabel = {"id":"ID*","name":"Nama kegiatan*","category":"Jenis Kegiatan*","speaker":"Pembicara","date":"Tanggal (dd-mm-yyyy)*","time":"Pukul (hh:mm)*","point":"Poin*","repetition":"Repetition*"}
    exec(f"frame_new_events_label_{i} = ttk.Label(frame_new_events_label, text='{dictLabel[i]}')")
    exec(f"frame_new_events_label_{i}.grid(row={no}, column=0, padx=5, pady=5, sticky='w')")
    exec(f"frame_new_events_entry_{i} = ttk.Entry(frame_new_events_label)")
    exec(f"frame_new_events_entry_{i}.grid(row={no}, column=1, padx=5, pady=5)")

# frame_new_events_label_id = ttk.Label(frame_new_events_label, text="ID:")
# frame_new_events_label_id.grid(row=0, column=0, padx=5, pady=5)
# frame_new_events_entry_id = ttk.Entry(frame_new_events_label)
# frame_new_events_entry_id.grid(row=0, column=1, padx=5, pady=5)
# frame_new_events_label_name = ttk.Label(frame_new_events_label, text="Nama kegiatan:")
# frame_new_events_label_name.grid(row=1, column=0, padx=5, pady=5)
# frame_new_events_entry_name = ttk.Entry(frame_new_events_label)
# frame_new_events_entry_name.grid(row=1, column=1, padx=5, pady=5)
# frame_new_events_label_category = ttk.Label(frame_new_events_label, text="Jenis kegiatan:")
# frame_new_events_label_category.grid(row=2, column=0, padx=5, pady=5)
# frame_new_events_entry_category = ttk.Entry(frame_new_events_label)
# frame_new_events_entry_category.grid(row=2, column=1, padx=5, pady=5)
# frame_new_events_label_speaker = ttk.Label(frame_new_events_label, text="Pembicara:")
# frame_new_events_label_speaker.grid(row=3, column=0, padx=5, pady=5)
# frame_new_events_entry_speaker = ttk.Entry(frame_new_events_label)
# frame_new_events_entry_speaker.grid(row=3, column=1, padx=5, pady=5)
# frame_new_events_label_date = ttk.Label(frame_new_events_label, text="Tanggal:")
# frame_new_events_label_date.grid(row=4, column=0, padx=5, pady=5)
# frame_new_events_entry_date = ttk.Entry(frame_new_events_label)
# frame_new_events_entry_date.grid(row=4, column=1, padx=5, pady=5)
# frame_new_events_label_time = ttk.Label(frame_new_events_label, text="Pukul:")
# frame_new_events_label_time.grid(row=5, column=0, padx=5, pady=5)
# frame_new_events_entry_time = ttk.Entry(frame_new_events_label)
# frame_new_events_entry_time.grid(row=5, column=1, padx=5, pady=5)
# frame_new_events_label_point = ttk.Label(frame_new_events_label, text="Poin:")
# frame_new_events_label_point.grid(row=6, column=0, padx=5, pady=5)
# frame_new_events_entry_point = ttk.Entry(frame_new_events_label)
# frame_new_events_entry_point.grid(row=6, column=1, padx=5, pady=5)
# frame_new_events_label_repetition = ttk.Label(frame_new_events_label, text="Max repetition:")
# frame_new_events_label_repetition.grid(row=7, column=0, padx=5, pady=5)
# frame_new_events_entry_repetition = ttk.Entry(frame_new_events_label)
# frame_new_events_entry_repetition.grid(row=7, column=1, padx=5, pady=5)

frame_new_events_label_required = ttk.Label(frame_new_events_label, text="*Required", foreground="black", justify="center")
frame_new_events_label_required.grid(row=8, column=1, columnspan=2, pady=5)
frame_new_events_label_result = ttk.Label(frame_new_events_label, text="", foreground="red", justify="center")
frame_new_events_label_result.grid(row=9, column=0, columnspan=2, pady=5)
frame_new_events_submit = ttk.Button(frame_new_events_label, text='Submit', command=lambda: submit_new_events())
frame_new_events_submit.grid(row=10, column=0, columnspan=2, pady=5)

frame_new_events.grid_columnconfigure(0, weight=1)
frame_new_events.grid_columnconfigure(1, weight=1)


""" Frame New Mahasiswa """
def input_year_validation(text):
    try:
        text = int(text)
        if not 1900 <= text <= 2100: raise ValueError
    except ValueError:
        frame_new_students_label_result.config(text="System: Input tidak valid.\nSilakan masukkan tahun yang benar.", foreground="red", justify="center")
    else: return text

def submit_new_students():
    if not (students_id := input_empty_validation(frame_new_students_entry_id.get(), "ID")) or not (students_id := input_unique_validation(frame_new_students_entry_id.get(), 'mahasiswa', 'ID')): return 
    if not (students_password := input_empty_validation(frame_new_students_entry_password.get(), "password")): return 
    if not (students_name := input_empty_validation(frame_new_students_entry_name.get(), "nama")): return 
    students_major, students_email, students_phone = frame_new_students_entry_major.get(), frame_new_students_entry_email.get(), frame_new_students_entry_phone.get()
    if not (students_enrollyear := input_year_validation(frame_new_students_entry_enrollyear.get())): return 
    frame_new_students_label_result.config(text="System: Mahasiswa telah berhasil ditambahkan!", foreground="green", justify="center")
    insert_values("mahasiswa", "id,password,name,major,email,phone_number,enrollment_year,points_earned",
                [(students_id, students_password, students_name.title(), students_major, students_email, students_phone, students_enrollyear, 0)])
    commit()
    list_box_students()
    load_all_data_students()
    delete_entry_new_students()

def delete_entry_new_students():
    for i in ("id","password","name","major","email","phone","enrollyear"):
        exec(f"frame_new_students_entry_{i}.delete(0, tk.END)")

frame_new_students_back = ttk.Button(frame_new_students, text='Back', command=back_to_admin)
frame_new_students_back.grid(row=0, column=0, padx=5, pady=5)
frame_new_students_label = ttk.LabelFrame(frame_new_students, text='New Student')
frame_new_students_label.grid(row=1, column=0, columnspan=2, pady=5)

for no, i in enumerate(("id","password","name","major","email","phone","enrollyear")):
    dictLabel = {"id":"ID*","password":"Password*","name":"Nama Mahasiswa*","major":"Jurusan","email":"Email","phone":"Nomor Telepon","enrollyear":"Tahun Masuk*"}
    exec(f"frame_new_students_label_{i} = ttk.Label(frame_new_students_label, text='{dictLabel[i]}')")
    exec(f"frame_new_students_label_{i}.grid(row={no}, column=0, padx=5, pady=5, sticky='w')")
    exec(f"frame_new_students_entry_{i} = ttk.Entry(frame_new_students_label)")
    exec(f"frame_new_students_entry_{i}.grid(row={no}, column=1, padx=5, pady=5)")

frame_new_students_label_required = ttk.Label(frame_new_students_label, text="*Required", foreground="black", justify="center")
frame_new_students_label_required.grid(row=7, column=1, columnspan=2, pady=5)
frame_new_students_label_result = ttk.Label(frame_new_students_label, text="", foreground="red", justify="center")
frame_new_students_label_result.grid(row=8, column=0, columnspan=2, pady=5)
frame_new_students_submit = ttk.Button(frame_new_students_label, text='Submit', command=lambda: submit_new_students())
frame_new_students_submit.grid(row=9, column=0, columnspan=2, pady=5)

frame_new_students.grid_columnconfigure(0, weight=1)
frame_new_students.grid_columnconfigure(1, weight=1)

""" Frame New Staff """
def submit_new_staffs():
    if not (staffs_id := input_empty_validation(frame_new_staffs_entry_id.get(), "ID")) or not (staffs_id := input_unique_validation(frame_new_staffs_entry_id.get(), 'staff', 'ID')): return 
    if not (staffs_password := input_empty_validation(frame_new_staffs_entry_password.get(), "password")): return 
    if not (staffs_name := input_empty_validation(frame_new_staffs_entry_name.get(), "nama")): return 
    staffs_position, staffs_email, staffs_phone = frame_new_staffs_entry_position.get(), frame_new_staffs_entry_email.get(), frame_new_staffs_entry_phone.get()
    if not (staffs_joining_date := input_date_validation(frame_new_staffs_entry_joining_date.get())): return 
    frame_new_staffs_label_result.config(text="System: Mahasiswa telah berhasil ditambahkan!", foreground="green", justify="center")
    insert_values("staff", "id,password,name,position,email,phone_number,joining_date",
                [(staffs_id, staffs_password, staffs_name.title(), staffs_position, staffs_email, staffs_phone, staffs_joining_date)])
    commit()
    list_box_staffs()
    load_all_data_staffs()
    delete_entry_new_staffs()

def delete_entry_new_staffs():
    for i in ("id","password","name","position","email","phone","joining_date"):
        exec(f"frame_new_staffs_entry_{i}.delete(0, tk.END)")

frame_new_staffs_back = ttk.Button(frame_new_staffs, text='Back', command=back_to_admin)
frame_new_staffs_back.grid(row=0, column=0, padx=5, pady=5)
frame_new_staffs_label = ttk.LabelFrame(frame_new_staffs, text='New Staff')
frame_new_staffs_label.grid(row=1, column=0, columnspan=2, pady=5)

for no, i in enumerate(("id","password","name","position","email","phone","joining_date")):
    dictLabel = {"id":"ID*","password":"Password*","name":"Nama Staff*","position":"Jurusan","email":"Email","phone":"Nomor Telepon","joining_date":"Tanggal Masuk*"}
    exec(f"frame_new_staffs_label_{i} = ttk.Label(frame_new_staffs_label, text='{dictLabel[i]}')")
    exec(f"frame_new_staffs_label_{i}.grid(row={no}, column=0, padx=5, pady=5, sticky='w')")
    exec(f"frame_new_staffs_entry_{i} = ttk.Entry(frame_new_staffs_label)")
    exec(f"frame_new_staffs_entry_{i}.grid(row={no}, column=1, padx=5, pady=5)")

frame_new_staffs_label_required = ttk.Label(frame_new_staffs_label, text="*Required", foreground="black", justify="center")
frame_new_staffs_label_required.grid(row=7, column=1, columnspan=2, pady=5)
frame_new_staffs_label_result = ttk.Label(frame_new_staffs_label, text="", foreground="red", justify="center")
frame_new_staffs_label_result.grid(row=8, column=0, columnspan=2, pady=5)
frame_new_staffs_submit = ttk.Button(frame_new_staffs_label, text='Submit', command=lambda: submit_new_staffs())
frame_new_staffs_submit.grid(row=9, column=0, columnspan=2, pady=5)

frame_new_staffs.grid_columnconfigure(0, weight=1)
frame_new_staffs.grid_columnconfigure(1, weight=1)


""" Frame Admin: Rekap """
# Label untuk memilih event
frame_rekap_home_button = ttk.Button(frame_check_attendance, text='🏠︎', width=0, command=lambda: show_frame('admin'))
frame_rekap_home_button.grid(row=0, column=0, padx=10, ipady=5, pady=5, sticky='w')
label_select_event = tk.Label(frame_check_attendance, text="Select Event:")
label_select_event.grid(row=0, column=1, sticky="w", padx=10)



# Mendapatkan data events dari database
cursor.execute("SELECT id, name FROM events")
events = cursor.fetchall()

# Membuat combobox untuk memilih event
event_names = [event[1] for event in events]
event_ids = [event[0] for event in events]
selected_event_id = tk.StringVar()
selected_event_combobox = ttk.Combobox(frame_check_attendance, values=event_names, textvariable=selected_event_id)
selected_event_combobox.grid(row=0, column=2, padx=10)
selected_event_combobox.set("Select an event")

# Menyiapkan canvas untuk diagram pie
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(5, 3))
plt.close()

# Fungsi untuk menampilkan diagram pie berdasarkan event yang dipilih
def update_pie_charts(event_name):
    # Mengambil data mahasiswa yang hadir
    cursor.execute(f"""
        SELECT m.id, m.name
        FROM mahasiswa m
        JOIN log_mahasiswa lm ON m.id = lm.id_mahasiswa
        JOIN events e ON lm.id_event = e.id
        WHERE e.name = %s
    """, (event_name,))
    mahasiswa_ikut = cursor.fetchall()
    
    # Mengambil total mahasiswa
    cursor.execute("""
        SELECT id, name FROM mahasiswa
    """)
    mahasiswa_total = cursor.fetchall()
    
    # Hitung mahasiswa yang tidak ikut
    mahasiswa_tidak_ikut = [m for m in mahasiswa_total if m not in mahasiswa_ikut]
    
    # Mengambil data staff yang hadir
    cursor.execute(f"""
        SELECT s.id, s.name
        FROM staff s
        JOIN log_staff ls ON s.id = ls.id_staff
        JOIN events e ON ls.id_event = e.id
        WHERE e.name = %s
    """, (event_name,))
    staff_ikut = cursor.fetchall()

    # Mengambil total staff
    cursor.execute("""
        SELECT id, name FROM staff
    """)
    staff_total = cursor.fetchall()
    
    # Hitung staff yang tidak ikut
    staff_tidak_ikut = [s for s in staff_total if s not in staff_ikut]

    # Update Pie Chart Mahasiswa
    mahasiswa_count = [len(mahasiswa_ikut), len(mahasiswa_tidak_ikut)]
    if sum(mahasiswa_count) == 0:  # Tidak ada data
        mahasiswa_count = [0, len(mahasiswa_total)]  # Semua dianggap tidak ikut
    ax1.clear()
    ax1.pie(mahasiswa_count, labels=["Mahasiswa Ikut", "Mahasiswa Tidak Ikut"], autopct='%1.1f%%', startangle=90)
    ax1.set_title("Keikutsertaan Mahasiswa")

    # Update Pie Chart Staff
    staff_count = [len(staff_ikut), len(staff_tidak_ikut)]
    if sum(staff_count) == 0:  # Tidak ada data
        staff_count = [0, len(staff_total)]  # Semua dianggap tidak ikut
    ax2.clear()
    ax2.pie(staff_count, labels=["Staff Ikut", "Staff Tidak Ikut"], autopct='%1.1f%%', startangle=90)
    ax2.set_title("Keikutsertaan Staff")

    # Render canvas untuk pie chart
    canvas.draw()


# Membuat canvas untuk menampilkan pie charts
canvas_frame = tk.Frame(frame_check_attendance)
canvas_frame.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

canvas = FigureCanvasTkAgg(fig, canvas_frame)
canvas.get_tk_widget().grid(row=0, column=0)

# Mengatur combobox callback untuk update pie chart
def on_event_select(event):
    selected_event_name = selected_event_combobox.get()
    if selected_event_name != "Select an event":
        update_pie_charts(selected_event_name)

# Set nilai default Combobox ke event pertama 
if event_names:
    selected_event_combobox.set(event_names[0])  
    update_pie_charts(event_names[0]) 

selected_event_combobox.bind("<<ComboboxSelected>>", on_event_select)


    
def run():
    show_frame('login')
    root.mainloop()
    


# main
adminD = {"admin123":"1234"}
run()




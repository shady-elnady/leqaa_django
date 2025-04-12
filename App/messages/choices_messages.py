from django.utils.translation import gettext_lazy as _


class ChoicesMessages:
    ############################ User Types #############################
    # User Types
    ADMIN = _("Admin")
    ADMINS = _("Admins")
    SUPER_USER = _("Super User")
    SUPER_USERS = _("Super Users")
    STUDENT = _("Student")
    STUDENTS = _("Students")
    LECTURER = _("Lecturer")
    LECTURERS = _("Lecturers")
    COLLEGE = _("College")
    COLLEGES = _("Colleges")
    STAFF = _("Staff")

    ############################ Jobs #############################
    # Jobs
    DOCTOR = _("Doctor")
    ENGINEER = _("Engineer")
    PROFESSOR = _("Professor")
    TEACHER = _("Teacher")
    TEACHERS = _("Teachers")

    ############################ Gender #############################
    # Gender
    MALE = _("Male")
    FEMALE = _("Female")

    ############################ Marital Status #############################
    # Marital Status
    VIRGIN = _("Virgin")
    BACHELOR = _("Bachelor")
    MARRIED = _("Married")
    WIDOWER = _("Widower")
    DIVORCDE = _("Divorde")

    ############################ Languages #############################
    # Languages
    ENGLISH = _("English")
    ARABIC = _("Arabic")
    ARABIC_EGYPT = _("Arabic Egypt")
    FRENCH = _("French")
    TURKISH = _("Turkish")

    ############################ State Types #############################
    # State Types
    TALUK = _("Taluk")
    VILLAGE = _("Village")  # القرية
    DISTRICT = _("District")  # المنطقة
    MANOR = _("Manor")  # عزبه
    RESIDENTIAL_QUARTER = _("Residential Quarter")  # حى سكنى
    HOUSING = _("Housing")  # مساكن
    FEUDALISM = _("Feudalism")  # اقطاعيه
    REGION = _("Region")  # منطقه

    ############################ Continents #############################
    # Continents
    AFRICA = _("Africa")
    ASIA = _("Asia")
    EUROPE = _("Europe")
    NORTH_AMERICA = _("North America")
    OCEANIA = _("Oceania")
    SOUTH_AMERICA = _("South America")
    ANTARCTICA = _("Antarctica")

    ############################ Week days #############################
    # Week days
    SATURDAY = _("Saturday")
    SUNDAY = _("Sunday")
    MONDAY = _("Monday")
    TUESDAY = _("Tuesday")
    WEDNESDAY = _("Wednesday")
    THURSDAY = _("Thursday")
    FRIDAY = _("Friday")

    ############################ Facility Types #############################
    # Facility Types
    LABORATORY = _("Laboratory")
    MAIN_LABORATORY = _("Main Laboratory")
    ASSOCIATIONS = _("Association")
    DISPENSARY = _("Dispensary")
    SCIENTIFIC_COMPANY = _("Scientific Company")
    PHARMACEUTICAL_COMPANY = _("Pharmaceutical Company")
    SUPPLIER = _("Supplier")
    DENTAL_CLINIC = _("Dental Clinic")
    PRIVATE_CLINIC = _("Private Clinic")
    GROCERY_STORE = _("Grocery Store")
    BOOKSTORE = _("Bookstore")
    COFFEE = _("Coffee")
    BAKERY = _("Bakery")
    DELICATESSEN = _("Delicatessen")
    SCHOOL = _("School")
    CAFE = _("Café")
    LAUNDROMAT = _("Laundromat")
    HOTEL = _("Hotel")
    BUTCHER = _("Butcher")
    SUPERMARKET = _("Supermarket")
    GIFT_SHOP = _("Gift Shop")
    FLOWER_SHOP = _("Flower Shop")
    SPORTING_GOODS_STORE = _("Sporting Goods Store")
    ELECTRONICS_STORE = _("Electronics Store")
    BARBER = _("Barber")
    PHARMACY = _("Pharmacy")
    MEDICAL_FACILITY = _("Medical Facility")
    MOBILE_NETWORK = _("Mobile Network Company")

    ############################ Scores #############################
    # Scores
    ONE = _("1")
    TWO = _("2")
    THREE = _("3")

    ############################ Runs #############################
    # Runs (Delivery/Pickup Timings)
    SAME_DAY = _("Same Day")
    NEXT_DAY = _("Next Day")
    AFTER_2_DAYS = _("After 2 Days")
    AFTER_4_DAYS = _("After 4 Days")
    AFTER_10_DAYS = _("After 10 Days")
    AFTER_WEEK = _("After Week")
    AFTER_2_WEEK = _("After Two Weeks")
    AFTER_MONTH = _("After Month")

    ############################ Product Transactions #############################
    # Product Transactions
    IMPORTED_PRODUCTS = _("Imported Products")
    EXPORTED_PRODUCTS = _("Exported Products")

    ############################ Platforms #############################
    # Platforms
    ANDROID = _("Android")
    IOS = _("iOS")
    WINDOWS = _("Windows")
    LINUX = _("Linux")
    BROWSER = _("Web Browser")

    ############################ Device Types #############################
    # Device Types
    MOBILE = _("Mobile")
    TABLET = _("Tablet")
    LAPTOP = _("Laptop")
    MAC = _("Mac")

    ############################ File Server Action #############################
    # File Server Action
    UPLOAD = _("Upload")
    DOWNLOAD = _("Download")

    ############################ File Types #############################
    # Parent & Child
    PARENT = _("Parent")
    CHILDREN = _("Children")
    ############################ CRUD Operations #############################
    CREATE = _("Create")
    UPDATE = _("Update")
    DELETE = _("Delete")
    GET = _("GET")
    POST = _("POST")
    PUT = _("PUT")
    PATCH = _("PATCH")

    ############################ Sign Types #############################
    SIGN_IN = _("Sign In")
    LOG_IN = _("Log In")
    SIGN_OUT = _("Sign Out")
    REGISTER = _("Register")

    ############################ LecturerFinancialSystem choices #############################
    # LecturerFinancialSystem choices
    ALL_EVENT = _("All Event")
    EACH_STUDENT = _("Each Student")
    ENLIST = _("Enlist")  # تطوع

    ############################ EventPaidStatus choices #############################
    # EventPaidStatus choices
    COMPLETELY_FREE = _("Completely Free")
    PARTIALLY_PAID = _("Partially Paid")
    COMPLETELY_PAID = _("Completely Paid")

    ############################ OnOrOffLineStatus choices #############################
    # OnOrOffLineStatus choices
    ON_LINE = _("On Line")
    OFF_LINE = _("Off Line")
    ANY = _("Any")

    ############################ OnOrOffLineStatus choices #############################
    # LecturerFinancialSystem choices
    ALL_EVENT = _("All Event")
    EACH_STUDENT = _("Each Student")
    ENLIST = _("Enlist")

    ############################ OnOrOffLineStatus choices #############################
    # EventPaidStatus choices
    COMPLETELY_FREE = _("Completely Free")
    PARTIALLY_PAID = _("Partially Paid")
    COMPLETELY_PAID = _("Completely Paid")

    ############################ OnOrOffLineStatus choices #############################
    # OnOrOffLineStatus choices
    ON_LINE = _("On Line")
    OFF_LINE = _("Off Line")
    ANY = _("Any")

    ############################ Reservation Status choices #############################
    INITIALIZATION_RESERVATION = _("Initialization Reservation")
    CANCELED_RESERVATION = _("Canceled Reservation")
    CONFIRMED_RESERVATION = _("Confirmed Reservation")
    HOLD_RESERVATION = _("Hold Reservation")
    ############################ Payment Method Types #############################
    MONETARY = _("Monetary")
    CREDIT_CARD = _("Credit Card")
    BANK_TRANSFER = _("Bank Transfer")
    CHECK = _("Check")
    MONEY_TRANSFER = _("Money Transfer")
    MOBILE_CASH = _("Mobile Cash")  # Fixed typo from "Cach" to "Cash"

    ############################ Payment Status Types #############################
    PAID = _("Paid")
    PAY_LATER = _("Pay later")
    PARTIALLY_PAID = _("Partially Paid")

    ############################ Financial Transaction Types #############################
    REVENUES = _("Revenues")  # الإيرادات
    EXPENSES = _("Expenses")  # المصروفات \ نفقات
    DEBTS = _("Debts")  # مديونيات
    DUES = _("Dues")  # مستحقات
    ############################ OnOrOffLineStatus choices #############################

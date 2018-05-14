const firstPad = function( num, length=2, char='0' ) {
    let strNum = num + "";
    while ( strNum.length < length ) {
        strNum = char + strNum;
    }
    return strNum;
};

const formatBool = function( value, positive="Да", negative="Нет" ) {
    return value ? positive : negative;
};

const formatDate = function( dateFromString, sep="/" ) {
    let date = new Date(dateFromString);
    let arrDate = [firstPad( date.getDate() ), firstPad( date.getMonth()+1 ), date.getFullYear()];
    return arrDate.join(sep);
};

const languageSettings = {
    "lengthMenu":       "Показывать по _MENU_ записей за раз",
    "decimal":        "",
    "emptyTable":     "Нет данных",
    "info":           "Показано c _START_ по _END_ из _TOTAL_ записи",
    "infoEmpty":      "Показано 0 записей",
    "infoFiltered":   "(показано из _MAX_ результатов)",
    "infoPostFix":    "",
    "thousands":      ",",
    "loadingRecords": "Идет загрузка...",
    "processing":     "Идет обработка...",
    "search":         "Поиск:",
    "zeroRecords":    "Нет совпадений",
    "paginate": {
        "first":      "Первая",
        "last":       "Последняя",
        "next":       "Следующая",
        "previous":   "Предыдущая"
    },
    select: {
        rows: {
            _: "",
            1: "Выбрана строка"
        }
    }
};

const redirectTo = path => window.location.href = path;
const zeroPad = function( num,length=2 ) {
    let strNum = num + "";
    while ( strNum.length < length ) {
        strNum = "0" + strNum;
    }
    return strNum;
};

const formatBool = function( value, positive="Да", negative="Нет" ) {
    return value ? positive : negative;
};

const formatDate = function( dateFromString ) {
    let date = new Date(dateFromString);
    return `${zeroPad( date.getDate() )}/${zeroPad( date.getMonth()+1 )}/${date.getFullYear()}`
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
};
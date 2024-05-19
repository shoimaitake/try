// CSRF対策
axios.defaults.xsrfHeaderName = "X-CSRFTOKEN"
axios.defaults.xsrfCookieName = "csrftoken"


document.addEventListener('DOMContentLoaded', function () {

    var calendarEl = document.getElementById('calendar');

    var calendar = new FullCalendar.Calendar(calendarEl, {
        initialView: 'timeGridWeek',
        // initialView: 'dayGridMonth',

        selectable: true,
        select: function(info) {
            const isConfirmed = confirm("この時間帯にスロットを追加しますか？");

            if (isConfirmed) {
                axios
                    .post("/add-slot/", {
                        start_time: info.start.valueOf(),
                        end_time: info.end.valueOf(),
                    })
                    .then(() => {
                        // イベントの追加
                        calendar.addEvent({
                            title: "slot",
                            start: info.start,
                            end: info.end,
                            allDay: false,
                        });
                    })
                    .catch(() => {
                        // バリデーションエラーなど
                        alert("登録に失敗しました");
                    });
            }
        },
        events: function (info, successCallback, failureCallback) {
            axios
                .post("/get-slot/", {
                    start_time: info.start.valueOf(),
                    end_time: info.end.valueOf(),
                })
                .then((response) => {
                    calendar.removeAllEvents();
                    successCallback(response.data);
                })
                .catch(() => {
                    // バリデーションエラーなど
                    alert("読み込みに失敗しました");
                });
        },
    });

    calendar.render();
});
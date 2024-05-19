document.addEventListener('DOMContentLoaded', function () {

    var calendarEl = document.getElementById('calendar');

    var calendar = new FullCalendar.Calendar(calendarEl, {
        initialView: 'timeGridWeek',

        selectable: true,
        select: function(info) {
            const eventName = prompt("スロットを入力してください");

            if (eventName) {
                calendar.addEvent({
                    title: eventName,
                    start: info.start,
                    end: info.end,
                    allDay: false,
                });
            }
        },
        // slotDuration: '00:15:00',
    });

    calendar.render();
});
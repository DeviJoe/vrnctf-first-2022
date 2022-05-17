# Одна большая кнопка

## Деплой

Static

## Описание

Всего лишь одна маленькая страница и одна большая кнопка (да и та зелёная). Что может быть проще...

## Решение 
```js
CryptoJS.AES.encrypt("vrnctf{b1g_gr33n_butt0n}", "the_best_review") + "";

            var review = prompt("Почти решилась... А пока решается, оставьте, пожалуйста, отзыв о задаче...");

            if (review != "th3_t4sk_17_b3s7") {
                alert ("Отзыв недостаточно хорош, так что и решения сегодня не будет...");
            }
            else {
                dc = CryptoJS.AES.decrypt("U2FsdGVkX18EjdQ2WrrB0N8Qg9JZoN38ThRIayvcgYbL2HenE6uwOTCQmrIALhk4", review + "_s4lt") + "";

                alert("Ну вот, бывают же хорошие отзывы... Вот вам и решение: " + dc);
            }
```
## Флаг
`vrnctf{b1g_gr33n_butt0n}`



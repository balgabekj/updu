# Updu — Приложение для полезных привычек в группах друзей

## 📱 Идея
Платформа, где друзья объединяются в группы, чтобы формировать привычки. Каждый участник должен ежедневно выкладывать фото своей активности, получать голосование от других и следить за стриками.

---

## 📌 Use Cases

### 1. Регистрация и вход
- Пользователь регистрируется и получает JWT токен.
- Вход с помощью username/email и пароля.

### 2. Создание и вступление в группу
- Пользователь создаёт группу.
- Другие участники могут присоединиться по коду/ссылке.

### 3. Публикация активности
- Участник загружает фото как доказательство выполнения действия.
- Указывает описание, выбирает группу.

### 4. Голосование
- Другие участники голосуют “да/нет”, была ли активность честной.

### 5. Комментарии
- Участники обсуждают пост в формате комментариев.

### 6. Система стриков
- Каждый день, если пост опубликован, streak увеличивается.
- Если день пропущен — streak сбрасывается.

---

## 🗃️ Модели данных

- **User**: username, email, avatar, streak_count
- **Group**: name, created_by, created_at
- **Post**: user, group, image, caption, created_at
- **Vote**: user, post, is_upvote
- **Comment**: user, post, text, created_at
- **Streak**: user, group, start_date, current_streak

![Полная ERD](updu_erd_diagram.png)

---

## 🧩 Технологии
- Django + Django REST Framework
- SimpleJWT
- PostgreSQL
- Deployed via Render / Railway / Vercel

---

## 🏁 MVP включает
- Регистрация / вход
- Создание группы
- Публикация поста
- Голосование и комментарии
- Подсчёт стрика

---

## 📂 Структура API


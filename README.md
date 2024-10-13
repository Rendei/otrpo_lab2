# Приложение для обнаружения лиц

Этот репозиторий содержит простое Python-приложение, которое использует библиотеку OpenCV для обнаружения лиц на заданном изображении. Приложение упаковано в Docker-контейнер, и контейнер можно собрать и отправить в DockerHub с помощью GitHub Actions.

## Требования

- Docker
- Аккаунт на DockerHub (для отправки образа)
- Аккаунт на GitHub

## Обзор приложения

Приложение читает изображение (`photo_1.jpg`) из репозитория и использует OpenCV для обнаружения лиц. Результат выводится в `stdout` (стандартный вывод).

### Файлы

- `face_detection.py`: Python-скрипт, который обнаруживает лица с использованием OpenCV.
- `photo.jpg`: Пример изображения, на котором происходит обнаружение лиц.
- `Dockerfile`: Dockerfile, используемый для сборки образа приложения.
- `.github/workflows/docker-publish.yml`: GitHub Actions workflow для сборки и отправки Docker-образа в DockerHub.

## Как собрать и запустить локально

1. **Клонируйте репозиторий**:

    ```bash
    git clone https://github.com/rendei/otrpo_python.git
    cd otrpo_python
    ```

2. **Соберите Docker-образ**:

    ```bash
    docker pull rendei/otrpo_python:latest
    ```

3. **Запустите Docker-контейнер**:

    ```bash
    docker run rendei/otrpo_python:latest
    ```

   После выполнения этой команды приложение обработает файл `photo.jpg` и выведет результат обнаружения лиц.

## GitHub Actions для автоматической сборки

Этот репозиторий настроен на автоматическую сборку и отправку Docker-образа в DockerHub с использованием GitHub Actions. Файл workflow расположен в `.github/workflows/docker-publish.yml`.

### Как настроить GitHub Actions для DockerHub

1. В репозитории на GitHub перейдите в `Settings` > `Secrets and variables` > `Actions`.
2. Добавьте следующие секреты:
   - `DOCKERHUB_USERNAME`: Ваше имя пользователя на DockerHub.
   - `DOCKERHUB_TOKEN`: Ваш токен доступа к DockerHub (или пароль).
   
3. Каждый раз, когда вы делаете push в ветку `main`, образ будет автоматически собираться и отправляться в DockerHub.

## Пример вывода

После запуска приложения в консоли отобразится количество обнаруженных лиц на изображении, например:

```bash
Found 1 face(s).
```

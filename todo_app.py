import click


class Cli:

    @click.group()
    def cli():
        pass

    @cli.command()
    @click.argument('task')
    def add(task):
        click.echo(f'Задача "{task}" успешно добавлена.')


if __name__ == '__main__':
    while True:
        user_input = input('Введите команду: ')
        Cli.cli(user_input.split())

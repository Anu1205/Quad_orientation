import click

@click.command()
@click.option('--file1', prompt='file name',
              help='The file to consider')

def countv(file1):

    """program that counts the no. of vowels in a text file."""


    v=["a","e","i","o","u"]
    f=open(file1,"r+")
    f1=f.read()
    global cnt
    cnt=0
    for i in f1.lower():
        if i in v:
            cnt=cnt+1
    #click.echo("the vowel count is :{}".format(cnt))
    print("the vowel count is :{}".format(cnt))
if __name__ == '__main__':
    countv()


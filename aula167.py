# locale para internacionalização (tradução)
# https://docs.python.org/3/library/locale.html
# https://learn.microsoft.com/fr-fr/powershell/module/international/get-winsystemlocale?view=windowsserver2022-ps&viewFallbackFrom=win10-ps
import calendar
import locale

# Ele vai alterar tudo desde datas, mas valores monetários, entre outros necessários por causa da categoria
# que está como LC_ALL e está buscando a localização do sistema operacional pois foi passado o atributo ''.


locale.setlocale(locale.LC_ALL, '')
# locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

print(calendar.calendar(2025))

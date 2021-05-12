def notas(*nums, sit=False):
    """
    --> Função para verificar as notas do aluno:
    :param nums: Notas que o usuário tem que digitar
    :param sit: [opcional] Se True, a situação em que o aluno está
    :return: Dicionário com todas as informações
    """

    infos = {'qntd_notas': len(nums), 'maior nota': max(nums), 'menor nota': min(nums), 'media_notas': sum(nums)/len(nums)}
    if sit:
        if sum(nums)/len(nums) >= 7:
            infos['situacao'] = 'BOM'
        elif sum(nums)/len(nums) >= 5:
            infos['situacao'] = 'RAZOÁVEL'
        else:
            infos['situacao'] = 'RUIM'
    return infos


print(notas(8, 5, 4, sit=False))


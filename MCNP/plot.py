def plot_flux2(energy, flux, color='blue', label='', error=None, ax=None, xscale='log', yscale='log', show=True):
    import matplotlib.pyplot as plt
    import numpy as np

    # Se um eixo iterável não for passado, cria uma figura nova
    if ax is None:
        fig, ax = plt.subplots(figsize=(9, 6))

    # O "Step plot" é o ideal para o MCNP pois representa melhor as bordas dos bins
    ax.step(energy, flux, where='post', linewidth=2.0, color=color, label=label)

    # Plota a incerteza estatística do MCNP como uma área sombreada (Standard deviation)
    if error is not None:
        # Como o Output padrão traz o erro relativo, multiplicamos pelo fluxo para ter o erro absoluto.
        # Caso a sua coluna 'error' já seja o absoluto, apenas use "abs_error = error"
        abs_error = flux * error 
        ax.fill_between(energy, flux - abs_error, flux + abs_error, 
                        step='post', color=color, alpha=0.3)

    # Escalas Logarítmicas ou Lineares
    ax.set_xscale(xscale)
    ax.set_yscale(yscale)

    # Textos e Rótulos
    ax.set_xlabel('Energy (MeV)', fontsize=16, fontfamily='serif')
    ax.set_ylabel('Flux (n.cm$^{-2}$.s$^{-1}$)', fontsize=16, fontfamily='serif')
    
    # Ticks maiores para combinar com o estilo científico
    ax.tick_params(axis='both', which='major', labelsize=14, width=2, length=7)
    ax.tick_params(axis='both', which='minor', width=1.5, length=4)
    
    # Grids, fundamentais para a leitura de espectros numa escala em Log
    ax.grid(True, which='major', linestyle='-', alpha=0.5, color='gray')
    ax.grid(True, which='minor', linestyle=':', alpha=0.4, color='gray')
    
    # Aumentar a espessura da caixa do gráfico
    for spine in ax.spines.values():
        spine.set_linewidth(1.5)

    if label:
        ax.legend(fontsize=14, frameon=True, edgecolor='black')
        
    if show:
        plt.tight_layout()
        plt.show()
        
    return ax
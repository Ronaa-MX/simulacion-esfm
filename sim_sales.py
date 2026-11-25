import pandas as pd
import numpy as np

# Fijar semilla aleatoria para asegurar resultados reproducibles
np.random.seed(42)

# 1. Cargar datos censales oficiales (CDMX)
df_census = pd.read_csv('PobDiscapacidad2020-CDMX.csv')

# Alcaldías seleccionadas de la Zona Norte y Centro
alcaldias_target = [
    'AZCAPOTZALCO', 'GUSTAVO A. MADERO', 'CUAUHTEMOC', 
    'VENUSTIANO CARRANZA', 'IZTACALCO', 'BENITO JUAREZ'
]

# Filtrar y calcular la población con discapacidad motriz total
df_target = df_census[df_census['alcaldia'].isin(alcaldias_target)]
pob_disc_motriz_zona = int(df_target['pob_disc_mot'].sum())  # 97,642 personas

# 2. Definición del horizonte temporal (Enero 2025 - Septiembre 2026)
fechas = pd.date_range(start='2025-01-01', end='2026-09-01', freq='MS')

# Factores de estacionalidad mensual
factores_estacionales = {
    1: 0.75, 2: 0.80, 3: 1.05, 4: 1.05, 5: 1.10, 6: 0.95,
    7: 0.90, 8: 0.95, 9: 1.20, 10: 1.25, 11: 1.20, 12: 1.10
}

meses_espanol = {
    1: 'Enero', 2: 'Febrero', 3: 'Marzo', 4: 'Abril', 5: 'Mayo', 6: 'Junio',
    7: 'Julio', 8: 'Agosto', 9: 'Septiembre', 10: 'Octubre', 11: 'Noviembre', 12: 'Diciembre'
}

n_sim = 10000
data_rows = []

# 3. Simulación Monte Carlo por mes
for fecha in fechas:
    year = fecha.year
    month = fecha.month
    f_est = factores_estacionales[month]
    
    # Parámetros epidemiológicos (distribuciones triangulares)
    t_amp = np.random.triangular(0.08, 0.10, 0.12, n_sim)    # 8% a 12% amputación inferior
    p_tfem = np.random.triangular(0.35, 0.40, 0.45, n_sim)   # 35% a 45% nivel transfemoral
    t_ren = np.random.triangular(0.06, 0.08, 0.10, n_sim)    # 6% a 10% renovación anual
    
    # Cuota de mercado (SOM) y capacidad según la etapa de la empresa
    if year == 2025:
        som = np.random.triangular(0.08, 0.11, 0.14, n_sim)
        cap_max = 5
    else:
        som = np.random.triangular(0.35, 0.42, 0.48, n_sim)
        cap_max = 20

    # Simulación de demanda mensual
    demanda_anual_sim = pob_disc_motriz_zona * t_amp * p_tfem * t_ren
    ventas_mc = (demanda_anual_sim * som * f_est) / 12.0
    
    # Obtener percentiles y convertir estrictamente a unidades enteras
    p10 = int(np.round(np.percentile(ventas_mc, 10)))
    p50 = int(np.round(np.percentile(ventas_mc, 50)))
    p90 = int(np.round(np.percentile(ventas_mc, 90)))
    
    # Venta asignada acotada por capacidad en números enteros
    val_entero = max(2 if year == 2025 else 8, min(p50, cap_max))
    
    data_rows.append({
        'Periodo': fecha.strftime('%Y-%m'),
        'Mes': f"{meses_espanol[month]} {year}",
        'Poblacion_Discapacidad_Motriz': pob_disc_motriz_zona,
        'Factor_Estacional': f_est,
        'Ventas_P10_Conservador': p10,
        'Ventas_P50_Esperado': p50,
        'Ventas_P90_Optimista': p90,
        'Ventas_Unidades_Simuladas': val_entero
    })

# 4. Exportar los resultados a CSV
df_resultado = pd.DataFrame(data_rows)
df_resultado.to_csv('Ventas_glbionic_2025_20264.csv', index=False, encoding='utf-8-sig')

print("Simulación ejecutada correctamente. Archivo 'Ventas_glbionic_2025_2026.csv' generado.")
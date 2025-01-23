# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['InterfaceGraphique.py'],
    pathex=['C:\\Users\\HP\\Documents\\Python'],  # Ajoutez le chemin du projet ici
    binaries=[],
 datas=[
    ('C:\\Users\\HP\\anaconda3\\Lib\\site-packages\\randomcolor\\lib\\colormap.json', 'randomcolor/lib'),
    ('C:\\Users\\HP\\anaconda3\\Lib\\site-packages\\matplotlib\\mpl-data', 'matplotlib/mpl-data'),
    ('emsi.jpeg', '.'),  # Inclure le fichier logo
],
    hiddenimports=['matplotlib', 'tkinter', 'PIL', 'PIL._imagingtk'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
    encoding='utf-8',  # Forcer l'encodage en UTF-8
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='InterfaceGraphique',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)

# player-mkchapter
video player para generar chapter en un archivo txt


## Notas

- agregado y carga de interfaz
- fix `drag and drop`
- set volume del player, al usar el slide no cambia el label
- se arreglo que el timer solo avance cuando se esta reproduciendo video
- se actualizo el `player_p6` a la ultima version del repositorio (con los fixs del slider de tiempo)
- se actualizan los labels de tiempo al usar el player (widget)
- se agrego tiempo restante a la interfaz


para arreglar `drag and drop` del widget player anidado:

```python
self.player.setAcceptDrops(False)
self.player.video_widget.setAttribute(Qt.WA_TransparentForMouseEvents, True)
```

en este caso aplique los cambios a la instancia del player
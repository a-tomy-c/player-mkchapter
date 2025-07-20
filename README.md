# player-mkchapter
video player para generar chapter en un archivo txt


## Notas

- agregado y carga de interfaz
- fix `drag and drop`
- set volume del player, al usar el slide no cambia el label
- se arreglo que el timer solo avance cuanod se esta reproduciendo video


para arreglar `drag and drop` del widget player anidado:

```python
self.player.setAcceptDrops(False)
self.player.video_widget.setAttribute(Qt.WA_TransparentForMouseEvents, True)
```

en este caso aplique los cambios a la instancia del player
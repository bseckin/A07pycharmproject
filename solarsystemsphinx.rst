Solarsystem
=================
Das Model repräsentiert die Zustände und Operationen der Anwendung. Das Model weiß nichts von Controllern und Views. Es
stellt aber Operationen bereit, die dann vom Controller zur Umsetzung von Ereignissen genutzt werden können, es
stellt Zustandsinformationen bereit, die dann vom View abgerufen werden können, um sie darzustellen und es
akzeptiert Anmeldungen von Ereignisempfängern und benachrichtigt diese über Änderungen seiner Zustände. Das wird vom View benutzt, um bei Änderungen die Darstellung aktualisieren zu können.

.. py:module:: a07Solarsystem.solarsystem
.. autoclass:: Solarsystem
	:members:

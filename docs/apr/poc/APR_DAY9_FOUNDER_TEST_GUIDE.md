# Internal Day 9 founder test

This is a nontechnical browser walkthrough for the internal Day 9 controlled instructional vertical slice. It is not formal Founder Alpha, R1A, pilot, learner validation, or Evidence collection.

## Start and log in
1. Start the application using the repository-established environment for APR POC review.
2. Log in with a user that has protected APR access.
3. Open `/apr/primeira-conexao`.
4. Open Lesson 1: `Enter the Connection`.

## Step 1: orientation
1. Confirm the title is `Entrar en la conexión`.
2. Confirm the first paragraph says a conversation starts by making space for another person.
3. Confirm `E você?` appears as the Portuguese invitation.
4. Continue without producing anything.

## Step 2: model, transcript, Bridge, and audio
1. Confirm the title is `Escucha una apertura`.
2. Confirm the model says exactly: `Oi! Eu sou a Marina. Gosto de música. E você?`
3. Select `Ver el texto` and confirm the transcript matches exactly.
4. Select `Ver el significado en español` and confirm the Spanish meaning is optional, not the dominant display.
5. Confirm `Puente desde el español` appears and returns to `Gosto de música.`
6. Confirm `Una prioridad de claridad` appears and focuses only on `vo-CÊ`.
7. Confirm `Haz espacio para la otra persona` appears.
8. Confirm the disclosure says: `Audio temporal generado para pruebas. No es la grabación final de la Academia.`
9. Request temporary audio and confirm it does not autoplay.
10. If TTS is unavailable, confirm the failure is technical and does not block continuing.

## Step 3: recognition
1. Continue to `Abre espacio para una respuesta`.
2. Try continuing without choosing; confirm the page asks you to select an option.
3. Choose the correct answer: `Comparte algo verdadero y termina con E você?`
4. Confirm the feedback explains that `E você?` opens space for participation.
5. In a separate run if useful, choose an incorrect answer and confirm the feedback points back to the final invitation without scoring.

## Step 4: spoken Practice
1. Confirm the prompt asks you to imagine meeting someone in an everyday context.
2. Confirm the frame is `Oi! Eu sou ________. Gosto de ________. E você?`
3. Confirm the privacy note says not to share private information.
4. Confirm the Practice notice says it does not create a grade, pronunciation evaluation, or level conclusion.
5. Start recording only when ready.
6. Confirm microphone permission is requested only after action.
7. Record an Original.
8. Play the Original.
9. Record again and confirm the Original remains while the new recording is shown as Latest retry.
10. If microphone access fails, confirm the copy says the failure is technical and offers retry, written Practice, or closing the session.

## Transcription and feedback
1. Request transcription for the Original.
2. Confirm the page says transcription is a technical aid and may be wrong.
3. Edit the machine draft.
4. Select `Confirmar este texto`.
5. Confirm the notice says confirming is not Evidence and not a score.
6. Request controlled feedback.
7. Confirm feedback is deterministic guidance, not a score, Evidence, pronunciation analysis, or Professor Gabriel.
8. Confirm no unconfirmed machine draft is sent for feedback.
9. In a separate run, do not confirm a transcript; select the static self-check and confirm no feedback API result is claimed.
10. If feedback fails, confirm the page says the technical aid was unavailable and continuation remains possible.

## Written Practice
1. In Step 4, select `Practicar por escrito`.
2. Confirm the notice says this route does not permit interpreting speech, pronunciation, or intelligibility.
3. Leave the field empty and confirm continuation is blocked.
4. Enter a Portuguese opening using the frame.
5. Confirm written Practice allows continuation.
6. Confirm it is not called spoken performance or formal Evidence.

## Step 5: reflection
1. Confirm the title is `Reflexiona`.
2. Confirm the prompt asks which block helped most: `Eu sou...`, `Gosto de...`, or `E você?`
3. Enter a short reflection.
4. Go back and forward and confirm the reflection remains.
5. Open closure and confirm the reflection remains until confirmed Restart.

## Session closure
1. Confirm the badge is `Resumen de esta sesión`.
2. Confirm the heading is `Tu práctica está lista para cerrar`.
3. Confirm the body says the session creates no grade, level conclusion, formal Evidence, or completion record.
4. Confirm the session-only summary reports technical activities without claiming mastery or capability.
5. Select Restart and cancel; confirm session state is preserved.
6. Select Restart and confirm; confirm session state and object URLs are cleared.
7. Select `Cerrar esta práctica`; confirm routing returns to `/apr/primeira-conexao`.

## Record defects
Record any defect with the step number, exact observed text, browser, whether TTS/STT was available, and whether the issue blocked safe exit.

import { AprLessonPlayer } from '@/components/apr/AprLessonPlayer'

export default function AprEnterTheConnectionLessonPage() {
  return (
    <main className="mx-auto flex w-full max-w-3xl flex-1 flex-col px-4 py-6 sm:px-6 lg:py-10">
      <AprLessonPlayer endpoint="/api/apr/modules/primeira-conexao/lessons/enter-the-connection" />
    </main>
  )
}

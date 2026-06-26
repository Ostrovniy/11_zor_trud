export interface VillageFact {
  label: string
  value: string
  icon: string // primeicons class, напр. 'pi pi-users'
}

export interface VillageInfo {
  name: string
  region: string
  history: string
  facts: VillageFact[]
}

export interface NewsItem {
  id: number
  title: string
  excerpt: string
  date: string // ISO, напр. '2026-06-20'
}

export interface GalleryItem {
  id: number
  title: string
  imageUrl?: string
}

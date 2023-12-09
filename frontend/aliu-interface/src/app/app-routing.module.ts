import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { SearchComponent } from './search/search.component';
import { AboutComponent } from './about/about.component';
import { ReportsComponent } from './reports/reports.component';
import { ArtObjectListComponent } from './art-object-list/art-object-list.component';
import { ArtObjectDetailComponent } from './art-object-detail/art-object-detail.component';

const routes: Routes = [
  { path: '', redirectTo: '/search', pathMatch: 'full' },
  { path: 'about', component: AboutComponent },
  { path: 'search', component: SearchComponent },
  { path: 'reports', component: ReportsComponent },
  { path: 'art-objects', component: ArtObjectListComponent },
  { path: 'art-object/:id', component: ArtObjectDetailComponent }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }

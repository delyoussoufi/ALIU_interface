import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { SearchComponent } from './search/search.component';
import { ArtObjectListComponent } from './art-object-list/art-object-list.component';
import { ArtObjectDetailComponent } from './art-object-detail/art-object-detail.component';
import { HeaderComponent } from './header/header.component';
import { FooterComponent } from './footer/footer.component';
import { AboutComponent } from './about/about.component';
import { ReportsComponent } from './reports/reports.component';

@NgModule({
  declarations: [
    AppComponent,
    SearchComponent,
    ArtObjectListComponent,
    ArtObjectDetailComponent,
    HeaderComponent,
    FooterComponent,
    AboutComponent,
    ReportsComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }

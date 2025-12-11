import { Button } from "@/components/ui/button";
import { ScrollArea } from "@/components/ui/scroll-area";
import { Separator } from "@/components/ui/separator";
import { cn } from "@/lib/utils";
import {
  BarChart3,
  Box,
  ChevronLeft,
  ChevronRight,
  Globe,
  History,
  Home,
  LayoutDashboard,
  LogOut,
  Menu,
  Search,
  Settings,
  User
} from "lucide-react";
import { useState } from "react";
import { Link, useLocation } from "wouter";

interface DashboardLayoutProps {
  children: React.ReactNode;
}

export function DashboardLayout({ children }: DashboardLayoutProps) {
  const [location] = useLocation();
  const [collapsed, setCollapsed] = useState(false);
  const [mobileMenuOpen, setMobileMenuOpen] = useState(false);

  const navItems = [
    { icon: LayoutDashboard, label: "Dashboard", href: "/" },
    { icon: Box, label: "Projetos", href: "/projetos" },
    { icon: Search, label: "Pesquisar", href: "/pesquisa" },
    { icon: History, label: "Histórico", href: "/historico" },
    { icon: User, label: "Perfil", href: "/perfil" },
    { icon: Settings, label: "Configurações", href: "/configuracoes" },
  ];

  return (
    <div className="min-h-screen bg-background flex font-roboto">
      {/* Sidebar */}
      <aside
        className={cn(
          "fixed inset-y-0 left-0 z-50 bg-sidebar text-sidebar-foreground transition-all duration-300 ease-in-out border-r border-sidebar-border shadow-xl",
          collapsed ? "w-[80px]" : "w-[280px]",
          mobileMenuOpen ? "translate-x-0" : "-translate-x-full lg:translate-x-0"
        )}
      >
        <div className="h-full flex flex-col">
          {/* Logo Area */}
          <div className="h-20 flex items-center justify-center border-b border-sidebar-border relative">
            <div className="flex items-center gap-3 px-4 w-full">
              <div className="bg-primary text-primary-foreground p-2 rounded-lg shrink-0">
                <Globe className="h-6 w-6" />
              </div>
              {!collapsed && (
                <span className="font-oswald font-bold text-xl tracking-wide truncate">
                  CHINA FÁCIL
                </span>
              )}
            </div>
            <Button
              variant="ghost"
              size="icon"
              className="absolute -right-3 top-1/2 -translate-y-1/2 bg-sidebar border border-sidebar-border rounded-full h-6 w-6 hidden lg:flex items-center justify-center shadow-md z-50 text-sidebar-foreground hover:bg-sidebar-accent hover:text-sidebar-accent-foreground"
              onClick={() => setCollapsed(!collapsed)}
            >
              {collapsed ? <ChevronRight className="h-3 w-3" /> : <ChevronLeft className="h-3 w-3" />}
            </Button>
          </div>

          {/* Navigation */}
          <ScrollArea className="flex-1 py-6">
            <nav className="px-3 space-y-2">
              {navItems.map((item) => {
                const isActive = location === item.href;
                return (
                  <Link key={item.href} href={item.href}>
                    <div
                      className={cn(
                        "flex items-center gap-3 px-3 py-3 rounded-lg cursor-pointer transition-all duration-200 group",
                        isActive
                          ? "bg-primary text-primary-foreground shadow-md"
                          : "text-sidebar-foreground/80 hover:bg-sidebar-accent hover:text-sidebar-accent-foreground"
                      )}
                    >
                      <item.icon className={cn("h-5 w-5 shrink-0", isActive ? "text-white" : "text-sidebar-foreground/60 group-hover:text-primary")} />
                      {!collapsed && (
                        <span className={cn("font-medium truncate", isActive ? "font-bold" : "")}>
                          {item.label}
                        </span>
                      )}
                      {isActive && !collapsed && (
                        <div className="ml-auto w-1.5 h-1.5 rounded-full bg-white" />
                      )}
                    </div>
                  </Link>
                );
              })}
            </nav>
          </ScrollArea>

          {/* User Profile Footer */}
          <div className="p-4 border-t border-sidebar-border bg-sidebar-accent/10">
            <div className={cn("flex items-center gap-3", collapsed ? "justify-center" : "")}>
              <div className="relative">
                <img 
                  src="/images/avatar-placeholder.jpg" 
                  alt="User" 
                  className="h-10 w-10 rounded-full border-2 border-primary object-cover"
                />
                <div className="absolute bottom-0 right-0 h-3 w-3 bg-green-500 rounded-full border-2 border-sidebar"></div>
              </div>
              {!collapsed && (
                <div className="flex-1 overflow-hidden">
                  <p className="text-sm font-bold truncate">Admin User</p>
                  <p className="text-xs text-muted-foreground truncate">admin@chinafacil.com</p>
                </div>
              )}
              {!collapsed && (
                <Button variant="ghost" size="icon" className="h-8 w-8 text-muted-foreground hover:text-destructive">
                  <LogOut className="h-4 w-4" />
                </Button>
              )}
            </div>
          </div>
        </div>
      </aside>

      {/* Mobile Overlay */}
      {mobileMenuOpen && (
        <div 
          className="fixed inset-0 bg-black/50 z-40 lg:hidden backdrop-blur-sm"
          onClick={() => setMobileMenuOpen(false)}
        />
      )}

      {/* Main Content */}
      <main 
        className={cn(
          "flex-1 transition-all duration-300 ease-in-out min-h-screen flex flex-col",
          collapsed ? "lg:ml-[80px]" : "lg:ml-[280px]"
        )}
      >
        {/* Mobile Header */}
        <header className="h-16 bg-card border-b border-border flex items-center px-4 lg:hidden sticky top-0 z-30 shadow-sm">
          <Button variant="ghost" size="icon" onClick={() => setMobileMenuOpen(true)}>
            <Menu className="h-6 w-6" />
          </Button>
          <span className="ml-3 font-oswald font-bold text-lg text-primary">CHINA FÁCIL</span>
        </header>

        {/* Page Content */}
        <div className="flex-1 p-4 md:p-8 overflow-x-hidden">
          <div className="max-w-7xl mx-auto w-full animate-in fade-in slide-in-from-bottom-4 duration-500">
            {children}
          </div>
        </div>
      </main>
    </div>
  );
}

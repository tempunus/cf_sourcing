import { DashboardLayout } from "@/components/DashboardLayout";
import { Button } from "@/components/ui/button";
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card";
import { Progress } from "@/components/ui/progress";
import { Separator } from "@/components/ui/separator";
import { 
  ArrowUpRight, 
  BarChart3, 
  Calendar, 
  CheckCircle2, 
  Clock, 
  Download, 
  FileText, 
  Filter, 
  MoreHorizontal, 
  PieChart, 
  Plus, 
  Search, 
  TrendingUp, 
  Users 
} from "lucide-react";
import { 
  Area, 
  AreaChart, 
  Bar, 
  BarChart, 
  CartesianGrid, 
  Cell, 
  Legend, 
  Line, 
  LineChart, 
  ResponsiveContainer, 
  Tooltip, 
  XAxis, 
  YAxis 
} from "recharts";

// Mock Data
const projectStatusData = [
  { name: "Em Análise", value: 12, color: "#D4AF37" },
  { name: "Em Cotação", value: 28, color: "#C8102E" },
  { name: "Aguardando Aprovação", value: 15, color: "#E57373" },
  { name: "Concluídos", value: 45, color: "#2C2C2C" },
];

const monthlyProjectsData = [
  { name: "Jan", projetos: 12, concluidos: 8 },
  { name: "Fev", projetos: 19, concluidos: 12 },
  { name: "Mar", projetos: 15, concluidos: 10 },
  { name: "Abr", projetos: 22, concluidos: 15 },
  { name: "Mai", projetos: 28, concluidos: 20 },
  { name: "Jun", projetos: 35, concluidos: 25 },
];

const recentProjects = [
  { id: "CF-2025-001", cliente: "TechSolutions Ltda", status: "Em Cotação", data: "09/12/2025", valor: "R$ 45.000" },
  { id: "CF-2025-002", cliente: "Importadora Brasil", status: "Concluído", data: "08/12/2025", valor: "R$ 120.000" },
  { id: "CF-2025-003", cliente: "Varejo Express", status: "Em Análise", data: "08/12/2025", valor: "R$ 15.500" },
  { id: "CF-2025-004", cliente: "Grupo Silva", status: "Aguardando", data: "07/12/2025", valor: "R$ 89.000" },
  { id: "CF-2025-005", cliente: "Mega Eletrônicos", status: "Em Cotação", data: "06/12/2025", valor: "R$ 210.000" },
];

export default function Home() {
  return (
    <DashboardLayout>
      {/* Header Section */}
      <div className="flex flex-col md:flex-row md:items-center justify-between gap-4 mb-6 md:mb-8">
        <div>
          <h1 className="text-2xl md:text-3xl font-oswald font-bold text-foreground tracking-tight">DASHBOARD GERAL</h1>
          <p className="text-sm md:text-base text-muted-foreground mt-1">Visão geral de performance e projetos ativos</p>
        </div>
        <div className="flex flex-col sm:flex-row gap-3 w-full md:w-auto">
          <Button variant="outline" className="w-full sm:w-auto gap-2 border-primary/20 hover:bg-primary/5 hover:text-primary justify-center">
            <Download className="h-4 w-4" />
            Exportar
          </Button>
          <Button className="w-full sm:w-auto gap-2 bg-primary hover:bg-primary/90 text-white shadow-lg shadow-primary/20 justify-center">
            <Plus className="h-4 w-4" />
            Novo Projeto
          </Button>
        </div>
      </div>

      {/* KPI Cards */}
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 mb-8">
        <Card className="border-l-4 border-l-primary shadow-sm hover:shadow-md transition-shadow">
          <CardContent className="p-6">
            <div className="flex justify-between items-start">
              <div>
                <p className="text-sm font-medium text-muted-foreground mb-1">Total de Projetos</p>
                <h3 className="text-3xl font-bold font-oswald">142</h3>
              </div>
              <div className="p-2 bg-primary/10 rounded-lg text-primary">
                <FileText className="h-5 w-5" />
              </div>
            </div>
            <div className="mt-4 flex items-center text-sm text-green-600">
              <TrendingUp className="h-4 w-4 mr-1" />
              <span className="font-medium">+12%</span>
              <span className="text-muted-foreground ml-1">vs mês anterior</span>
            </div>
          </CardContent>
        </Card>

        <Card className="border-l-4 border-l-[#D4AF37] shadow-sm hover:shadow-md transition-shadow">
          <CardContent className="p-6">
            <div className="flex justify-between items-start">
              <div>
                <p className="text-sm font-medium text-muted-foreground mb-1">Em Andamento</p>
                <h3 className="text-3xl font-bold font-oswald">45</h3>
              </div>
              <div className="p-2 bg-[#D4AF37]/10 rounded-lg text-[#D4AF37]">
                <Clock className="h-5 w-5" />
              </div>
            </div>
            <div className="mt-4 flex items-center text-sm text-muted-foreground">
              <span className="font-medium text-foreground">32%</span>
              <span className="ml-1">do total de projetos</span>
            </div>
          </CardContent>
        </Card>

        <Card className="border-l-4 border-l-[#2C2C2C] shadow-sm hover:shadow-md transition-shadow">
          <CardContent className="p-6">
            <div className="flex justify-between items-start">
              <div>
                <p className="text-sm font-medium text-muted-foreground mb-1">Concluídos</p>
                <h3 className="text-3xl font-bold font-oswald">89</h3>
              </div>
              <div className="p-2 bg-[#2C2C2C]/10 rounded-lg text-[#2C2C2C]">
                <CheckCircle2 className="h-5 w-5" />
              </div>
            </div>
            <div className="mt-4 flex items-center text-sm text-green-600">
              <TrendingUp className="h-4 w-4 mr-1" />
              <span className="font-medium">+5%</span>
              <span className="text-muted-foreground ml-1">taxa de conversão</span>
            </div>
          </CardContent>
        </Card>

        <Card className="border-l-4 border-l-[#E57373] shadow-sm hover:shadow-md transition-shadow">
          <CardContent className="p-6">
            <div className="flex justify-between items-start">
              <div>
                <p className="text-sm font-medium text-muted-foreground mb-1">Novos Clientes</p>
                <h3 className="text-3xl font-bold font-oswald">18</h3>
              </div>
              <div className="p-2 bg-[#E57373]/10 rounded-lg text-[#E57373]">
                <Users className="h-5 w-5" />
              </div>
            </div>
            <div className="mt-4 flex items-center text-sm text-green-600">
              <ArrowUpRight className="h-4 w-4 mr-1" />
              <span className="font-medium">+3</span>
              <span className="text-muted-foreground ml-1">esta semana</span>
            </div>
          </CardContent>
        </Card>
      </div>

      {/* Charts Section */}
      <div className="grid grid-cols-1 lg:grid-cols-3 gap-6 mb-8">
        {/* Main Chart */}
        <Card className="lg:col-span-2 shadow-sm">
          <CardHeader>
            <CardTitle className="font-oswald text-xl">Evolução de Projetos (Semestral)</CardTitle>
            <CardDescription>Comparativo entre novos projetos e conclusões</CardDescription>
          </CardHeader>
          <CardContent>
            <div className="h-[300px] w-full">
              <ResponsiveContainer width="100%" height="100%">
                <AreaChart data={monthlyProjectsData} margin={{ top: 10, right: 30, left: 0, bottom: 0 }}>
                  <defs>
                    <linearGradient id="colorProjetos" x1="0" y1="0" x2="0" y2="1">
                      <stop offset="5%" stopColor="#C8102E" stopOpacity={0.8}/>
                      <stop offset="95%" stopColor="#C8102E" stopOpacity={0}/>
                    </linearGradient>
                    <linearGradient id="colorConcluidos" x1="0" y1="0" x2="0" y2="1">
                      <stop offset="5%" stopColor="#2C2C2C" stopOpacity={0.8}/>
                      <stop offset="95%" stopColor="#2C2C2C" stopOpacity={0}/>
                    </linearGradient>
                  </defs>
                  <XAxis dataKey="name" axisLine={false} tickLine={false} />
                  <YAxis axisLine={false} tickLine={false} />
                  <CartesianGrid vertical={false} strokeDasharray="3 3" stroke="#eee" />
                  <Tooltip 
                    contentStyle={{ borderRadius: '8px', border: 'none', boxShadow: '0 4px 12px rgba(0,0,0,0.1)' }}
                  />
                  <Legend />
                  <Area type="monotone" dataKey="projetos" stroke="#C8102E" fillOpacity={1} fill="url(#colorProjetos)" name="Novos Projetos" />
                  <Area type="monotone" dataKey="concluidos" stroke="#2C2C2C" fillOpacity={1} fill="url(#colorConcluidos)" name="Concluídos" />
                </AreaChart>
              </ResponsiveContainer>
            </div>
          </CardContent>
        </Card>

        {/* Status Chart */}
        <Card className="shadow-sm">
          <CardHeader>
            <CardTitle className="font-oswald text-xl">Status Atual</CardTitle>
            <CardDescription>Distribuição por fase</CardDescription>
          </CardHeader>
          <CardContent>
            <div className="h-[200px] w-full mb-6">
              <ResponsiveContainer width="100%" height="100%">
                <BarChart data={projectStatusData} layout="vertical" margin={{ top: 0, right: 30, left: 40, bottom: 0 }}>
                  <XAxis type="number" hide />
                  <YAxis dataKey="name" type="category" width={100} hide />
                  <Tooltip cursor={{fill: 'transparent'}} />
                  <Bar dataKey="value" radius={[0, 4, 4, 0]} barSize={20}>
                    {projectStatusData.map((entry, index) => (
                      <Cell key={`cell-${index}`} fill={entry.color} />
                    ))}
                  </Bar>
                </BarChart>
              </ResponsiveContainer>
            </div>
            <div className="space-y-4">
              {projectStatusData.map((item, index) => (
                <div key={index} className="flex items-center justify-between">
                  <div className="flex items-center gap-2">
                    <div className="w-3 h-3 rounded-full" style={{ backgroundColor: item.color }} />
                    <span className="text-sm font-medium">{item.name}</span>
                  </div>
                  <div className="flex items-center gap-2">
                    <span className="text-sm font-bold">{item.value}%</span>
                    <Progress value={item.value} className="w-16 h-2" style={{ "--progress-background": item.color } as React.CSSProperties} />
                  </div>
                </div>
              ))}
            </div>
          </CardContent>
        </Card>
      </div>

      {/* Recent Projects Table */}
      <Card className="shadow-sm overflow-hidden">
        <CardHeader className="flex flex-row items-center justify-between bg-muted/30">
          <div>
            <CardTitle className="font-oswald text-xl">Projetos Recentes</CardTitle>
            <CardDescription>Últimas atualizações no sistema</CardDescription>
          </div>
          <div className="flex gap-2">
            <div className="relative">
              <Search className="absolute left-2.5 top-2.5 h-4 w-4 text-muted-foreground" />
              <input 
                type="text" 
                placeholder="Buscar projeto..." 
                className="pl-9 h-9 w-64 rounded-md border border-input bg-background px-3 py-1 text-sm shadow-sm transition-colors focus-visible:outline-none focus-visible:ring-1 focus-visible:ring-ring"
              />
            </div>
            <Button variant="outline" size="icon">
              <Filter className="h-4 w-4" />
            </Button>
          </div>
        </CardHeader>
        <CardContent className="p-0">
          <div className="overflow-x-auto">
            <table className="w-full text-sm text-left">
              <thead className="text-xs text-muted-foreground uppercase bg-muted/50 border-b">
                <tr>
                  <th className="px-4 md:px-6 py-3 font-medium whitespace-nowrap">ID Projeto</th>
                  <th className="px-4 md:px-6 py-3 font-medium whitespace-nowrap">Cliente</th>
                  <th className="px-4 md:px-6 py-3 font-medium whitespace-nowrap">Data</th>
                  <th className="px-4 md:px-6 py-3 font-medium whitespace-nowrap">Valor Est.</th>
                  <th className="px-4 md:px-6 py-3 font-medium whitespace-nowrap">Status</th>
                  <th className="px-4 md:px-6 py-3 font-medium text-right whitespace-nowrap">Ações</th>
                </tr>
              </thead>
              <tbody>
                {recentProjects.map((project, index) => (
                  <tr key={index} className="bg-white border-b hover:bg-muted/20 transition-colors">
                    <td className="px-4 md:px-6 py-3 md:py-4 font-medium text-primary whitespace-nowrap">{project.id}</td>
                    <td className="px-4 md:px-6 py-3 md:py-4 font-medium whitespace-nowrap">{project.cliente}</td>
                    <td className="px-4 md:px-6 py-3 md:py-4 text-muted-foreground whitespace-nowrap">{project.data}</td>
                    <td className="px-4 md:px-6 py-3 md:py-4 font-medium whitespace-nowrap">{project.valor}</td>
                    <td className="px-4 md:px-6 py-3 md:py-4 whitespace-nowrap">
                      <span className={`px-2.5 py-0.5 rounded-full text-xs font-medium border ${
                        project.status === 'Concluído' ? 'bg-green-100 text-green-800 border-green-200' :
                        project.status === 'Em Cotação' ? 'bg-blue-100 text-blue-800 border-blue-200' :
                        project.status === 'Em Análise' ? 'bg-yellow-100 text-yellow-800 border-yellow-200' :
                        'bg-gray-100 text-gray-800 border-gray-200'
                      }`}>
                        {project.status}
                      </span>
                    </td>
                    <td className="px-4 md:px-6 py-3 md:py-4 text-right whitespace-nowrap">
                      <Button variant="ghost" size="icon" className="h-8 w-8">
                        <MoreHorizontal className="h-4 w-4" />
                      </Button>
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        </CardContent>
      </Card>
    </DashboardLayout>
  );
}
